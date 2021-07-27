import glfw
from camera import Camera

# Clase controlador con variables para manejar el estado de ciertos botones
class Controller:
    def __init__(self):
        self.fillPolygon = True
        self.showAxis = True

        # Variables para controlar la camara
        self.is_w_pressed = False       # tecla w
        self.is_s_pressed = False       # tecla s
        self.is_a_pressed = False       # tecla a
        self.is_d_pressed = False       # tecla d
        self.is_q_pressed = False       # tecla q
        self.is_e_pressed = False       # tecla e 
        self.is_left_pressed = False    # tecla izq
        self.is_right_pressed = False   # tecla der
        self.is_up_pressed = False      # tecla up
        self.is_down_pressed = False    # tecla down
        self.is_space_pressed = False   # espacio

        self.indice_tecnica = 0         # indice de tecnica de EDO
        self.firstPerson = False        # primera persona       
        self.selectedBall = 15          # indice de bola objetivo
        self.ballList = []              # lista con todas las bolas
        self.fuerza = 0                 # fuerza del taco
        self.canHit = True              # el taco puede golpear
        self.followBall = False         # se sigue a la bola golpeada
        self.tambalear = False          # la barra deberia tambalear
        self.roce = 0                   # coef roce
        self.restitucion = 0            # coef restitucion

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
    if key == glfw.KEY_E:
        if action == glfw.PRESS:
            self.is_e_pressed = True
        elif action == glfw.RELEASE:
            self.is_e_pressed = False

    # Caso de detectar la tecla [Izquierda], actualiza estado de variable
    if key == glfw.KEY_LEFT:
        if action == glfw.PRESS:
            self.is_left_pressed = True
        elif action == glfw.RELEASE:
            self.is_left_pressed = False

    # Caso de detectar la tecla [Derecha], actualiza estado de variable
    if key == glfw.KEY_RIGHT:
        if action == glfw.PRESS:
            self.is_right_pressed = True
        elif action == glfw.RELEASE:
            self.is_right_pressed = False

    # Caso de detectar la tecla [Up], actualiza estado de variable
    if key == glfw.KEY_UP:
        if action == glfw.PRESS:
            self.is_up_pressed = True
        elif action == glfw.RELEASE:
            self.is_up_pressed = False

    # Caso de detectar la tecla [Down], actualiza estado de variable
    if key == glfw.KEY_DOWN:
        if action == glfw.PRESS:
            self.is_down_pressed = True
        elif action == glfw.RELEASE:
            self.is_down_pressed = False

    # Caso de detectar la tecla [Space], actualiza estado de variable
    if key == glfw.KEY_SPACE:
        if action == glfw.PRESS:
            self.is_space_pressed = True
            self.tambalear = not self.tambalear
        elif action == glfw.RELEASE:
            self.is_space_pressed = False
    
    # Caso de detectar la barra espaciadora, se cambia el metodo de dibujo
    if key == glfw.KEY_SPACE:
        if action == glfw.PRESS:
            self.fillPolygon = not self.fillPolygon

    # Caso de detectar el numero 1
    if key == glfw.KEY_1:
        if action == glfw.PRESS:
            self.firstPerson = not self.firstPerson

    # Caso de detectar el numero 2
    if key == glfw.KEY_2:
        if action == glfw.PRESS:
            self.indice_tecnica = (self.indice_tecnica + 1) % 4

    # Caso de detectar el numero 3
    if key == glfw.KEY_3:
        if action == glfw.PRESS:
            self.selectedBall = (self.selectedBall + 1) % 16

    # Caso de detectar el numero 4
    if key == glfw.KEY_4:
        if action == glfw.PRESS:
            self.followBall = not self.followBall
                
    # Caso en que se cierra la ventana
    if key == glfw.KEY_ESCAPE:
        if action == glfw.PRESS:
            glfw.set_window_should_close(window, True)

