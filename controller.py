import glfw
from camera import Camera

# Clase controlador con variables para manejar el estado de ciertos botones
class Controller:
    def __init__(self):
        self.fillPolygon = True
        self.showAxis = True

        # Variables para controlar la camara
        self.is_w_pressed = False
        self.is_s_pressed = False
        self.is_a_pressed = False
        self.is_d_pressed = False
        self.is_q_pressed = False
        self.is_e_pressed = False
        self.is_tab_pressed = False
        self.manual = True
        self.slow = False
        self.is_3_pressed = False
        self.theta = 0
        self.mousePos = (0, 0)

# Metodo para leer la posicion del mouse
def cursor_pos_callback(self, window, x, y):
    self.mousePos = (x,y)

# Metodo para leer el input del teclado
def on_key(self, window, key, scancode, action, mods):

    # Caso de detectar la tecla [W], actualiza estado de variable
    if key == glfw.KEY_W:
        if action == glfw.PRESS:
            self.is_w_pressed = True
        elif action == glfw.RELEASE:
            self.is_w_pressed = False

    # Caso de detectar la tecla [S], actualiza estado de variable
    if key == glfw.KEY_S:
        if action == glfw.PRESS:
            self.is_s_pressed = True
        elif action == glfw.RELEASE:
            self.is_s_pressed = False

    # Caso de detectar la tecla [D], actualiza estado de variable
    if key == glfw.KEY_D:
        if action == glfw.PRESS:
            self.is_d_pressed = True
        elif action == glfw.RELEASE:
            self.is_d_pressed = False

    # Caso de detectar la tecla [A], actualiza estado de variable
    if key == glfw.KEY_A:
        if action == glfw.PRESS:
            self.is_a_pressed = True
        elif action == glfw.RELEASE:
            self.is_a_pressed = False

    # Caso de detectar la tecla [Q], actualiza estado de variable
    if key == glfw.KEY_Q:
        if action == glfw.PRESS:
            self.is_q_pressed = True
        elif action == glfw.RELEASE:
            self.is_q_pressed = False

    # Caso de detectar la tecla [E], actualiza estado de variable
    if key == glfw.KEY_A:
        if action == glfw.PRESS:
            self.is_e_pressed = True
        elif action == glfw.RELEASE:
            self.is_e_pressed = False
    
    # Caso de detectar la barra espaciadora, se cambia el metodo de dibujo
    if key == glfw.KEY_SPACE:
        if action == glfw.PRESS:
            self.fillPolygon = not self.fillPolygon

    # Caso de detectar el tab se cambian los pipelines
    if key == glfw.KEY_TAB:
        if action == glfw.PRESS:
            self.is_tab_pressed = not self.is_tab_pressed

    # Caso de detectar el numero 1
    if key == glfw.KEY_1:
        if action == glfw.PRESS:
            self.slow = not self.slow  

    # Caso de detectar el numero 2
    if key == glfw.KEY_2:
        if action == glfw.PRESS:
            self.manual = not self.manual

    # Caso de detectar el numero 3
    if key == glfw.KEY_3:
        if action == glfw.PRESS:
            self.is_3_pressed = not self.is_3_pressed                

    # Caso en que se cierra la ventana
    if key == glfw.KEY_ESCAPE:
        if action == glfw.PRESS:
            glfw.set_window_should_close(window, True)

