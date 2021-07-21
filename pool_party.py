import glfw
import math
import time
import OpenGL.GL.shaders
import grafica.performance_monitor as pm
import LightShaders as ls
import grafica.transformations as tr
import nodes as nd
from controller import Controller, on_key, cursor_pos_callback
from light import Light
from camera import Camera
from gameobject import GameObject
from shapes3d import *
from OpenGL.GL import *

"""Joaquín Uribe """

if __name__ == "__main__":

    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 1422 #1920
    height = 800 #1080
    title = "Pool party"

    window = glfw.create_window(width, height, title, None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)


    controller = Controller()
    def on_key_wrapper(window, key, scancode, action, mods):
        on_key(controller, window, key, scancode, action, mods)

    def cursor_pos_callback_wrapper(window, x, y):
        cursor_pos_callback(controller, window, x, y)


    # Se conecta la funcion de callback "cursos_pos_callback_wrapper" para ver la pos del mouse
    glfw.set_cursor_pos_callback(window, cursor_pos_callback_wrapper)

    # Connecting the callback function 'on_key_wrapper' to handle keyboard events
    glfw.set_key_callback(window, on_key_wrapper)

    # Pipeline con shaders con multiples fuentes de luz
    phongPipeline = ls.MultiplePhongShaderProgram()

    phongTexPipeline = ls.SimpleTexturePhongShaderProgram()

    # Se decide que tipo de luces se van a usar
    phong = phongPipeline
    phongTex = phongTexPipeline
    # Setting up the clear screen color
    glClearColor(0, 42/255, 42/255, 53/255) # color cielo oscuro

    # As we work in 3D, we need to check which part is in front,
    # and which one is at the back
    glEnable(GL_DEPTH_TEST)
    glLineWidth(10)

    # Se instancia la camara
    camera = Camera(controller)
    camera.setProjection(tr.perspective(60, float(width) / float(height), 0.1, 100))

    perfMonitor = pm.PerformanceMonitor(glfw.get_time(), 0.5)
    # glfw will swap buffers as soon as possible
    glfw.swap_interval(0)

    t0 = target_time = glfw.get_time()
    t_inicial = glfw.get_time()
    loop_delta = 1./60

    # Se instancian las luces que se van a utilizar
    lights = []

    light1 = Light(controller)
    lights.append(light1)
    # Las pipelines que se dan aqui son solo las default, luego se pueden cambiar
    #Maru = nd.createCharacter(celPipeline, celTexPipeline, controller)
    #scene = nd.createScene(celPipeline, celTexPipeline)
    bolas = nd.createBalls(phongTex)
    mesa = nd.createTable(phongTex)

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

        # Se cambian las luces entre spot y normales
        if (controller.is_3_pressed == True):
            phong = phongSpotPipeline
            phongTex = phongTexSpotPipeline
            cel = celSpotPipeline
            celTex = celTexSpotPipeline
        else:
            phong = phongPipeline
            phongTex = phongTexPipeline  

        # Se cambia entre phong y cel
        if (controller.is_tab_pressed):
            bolas.childs[0].addSpeed([0.8, 0.8])
        #else:
        #    Maru.changeTreesPipeline(cel, celTex)
        #    scene.changeTreesPipeline(cel, celTex)

        ########          Luz         #######
        for light in lights:
            light.update(delta)

        ########          Dibujo          ########
        #scene.update(delta, camera, lights)
        #Maru.update(delta, camera, lights)
        bolas.update(delta, camera, lights)
        mesa.update(delta, camera, lights)
        # Once the drawing is rendered, buffers are swap so an uncomplete drawing is never seen.
        glfw.swap_buffers(window)

        #Manejo del sleep
        target_time += loop_delta
        sleep_time = target_time - glfw.get_time()
        if sleep_time > 0:
            time.sleep(sleep_time)

    #scene.clear()
    #Maru.clear()

    glfw.terminate()