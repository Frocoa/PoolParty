import glfw
import math
import time
import OpenGL.GL.shaders
import json
import grafica.performance_monitor as pm
from BilliardBalls import Bball
import LightShaders as ls
import grafica.transformations as tr
import nodes as nd
from controller import Controller, on_key, cursor_pos_callback
from light import Light
from camera import Camera
from gameobject import GameObject
from shapes3d import *
from OpenGL.GL import *
import sys

archivo = sys.argv[1]

"""Joaquín Uribe"""

if __name__ == "__main__":

    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 1422 #1920
    height = 924 #1080
    title = "Pool party"
    glfw.window_hint(glfw.SAMPLES, 16)

    window = glfw.create_window(width, height, title, None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)

    #Opening JSON file
    f = open(archivo,)

    config = json.load(f)
    Dict = config['values'][0]

    f.close()

    controller = Controller()
    controller.roce = float(Dict['roce'])

    controller.restitucion = float(Dict['restitucion'])

    def on_key_wrapper(window, key, scancode, action, mods):
        on_key(controller, window, key, scancode, action, mods)

    def cursor_pos_callback_wrapper(window, x, y):
        cursor_pos_callback(controller, window, x, y)

    # Se conecta la funcion de callback "cursor_pos_callback_wrapper" para ver la pos del mouse
    glfw.set_cursor_pos_callback(window, cursor_pos_callback_wrapper)

    # Connecting the callback function 'on_key_wrapper' to handle keyboard events
    glfw.set_key_callback(window, on_key_wrapper)

    # Pipeline con shaders de iluminacion phongPipeline
    phongPipeline = ls.SimplePhongShaderProgram()
    phongTexPipeline = ls.SimpleTexturePhongShaderProgram()
    barTexPipeline = ls.BarTexturePhongShaderProgram()

    # Setting up the clear screen color
    glClearColor(10/255, 65/255, 68/255, 0) # color cielo oscuro

    # As we work in 3D, we need to check which part is in front,
    # and which one is at the back
    glEnable(GL_DEPTH_TEST)
    glLineWidth(10)

    # Activando transparencias
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    # Se instancia la camara
    camera = Camera(controller)
    camera.height = float(height)
    camera.width = float(width)

    perfMonitor = pm.PerformanceMonitor(glfw.get_time(), 0.5)

    # glfw will swap buffers as soon as possible
    glfw.swap_interval(0)

    t0 = target_time = glfw.get_time()
    t_inicial = glfw.get_time()
    loop_delta = 1./60

    # Se instancian las luces que se van a utilizar (es una lista porque se podrian poner varias luces)
    lights = []
    light1 = Light(controller)
    lights.append(light1)

    # Las pipelines que se dan aqui son solo las default, luego se pueden cambiar
    scene = nd.createScene(phongPipeline, phongTexPipeline, barTexPipeline, controller)

    # Application loop
    while not glfw.window_should_close(window):
        # Variables del tiempo
        t1 = glfw.get_time()
        delta = t1 -t0
        t0 = t1

        # Using GLFW to check for input events
        glfw.poll_events()

        #actualizar posicion de la camera y matriz de vista
        camera.update(delta)
        
        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Agregando el rendimiento
        perfMonitor.update(glfw.get_time())
        glfw.set_window_title(window, title + str(perfMonitor))


        ########          Luz         #######
        for light in lights:
            light.update(delta)

        ########          Dibujo          ########
        scene.update(delta, camera, lights)

        # Once the drawing is rendered, buffers are swap so an uncomplete drawing is never seen.
        glfw.swap_buffers(window)

        #Manejo del sleep
        target_time += loop_delta
        sleep_time = target_time - glfw.get_time()
        if sleep_time > 0:
            time.sleep(sleep_time)

    glfw.terminate()