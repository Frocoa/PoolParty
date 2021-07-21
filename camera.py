import numpy as np
import grafica.transformations as tr
import curves as cv
import math

# Clase para manejar una camara que se mueve en coordenadas polares
class Camera:
    
    def __init__(self, controller):
        self.controller = controller
        self.at = np.array([0.0, 0.0, 2])     # donde mira la camara
        self.position = np.array([-4.96, -5.0, 2])     # posicion de la camara
        self.eye = self.position                 # vector eye
        self.up = np.array([0, 0, 1])            # vector up
        self.viewMatrix = None                   # Matriz de vista
        self.projection = None                   # Matriz de proyeccion
        self.N = 1200                            # Cantidad de puntos en las curvas
        self.index = 1                           # Posicion de las curvas en las que se encuentra la camara
        self.objective = None                    # A que objeto mantiene siempre en la mira
        self.speed = 0.15
        self.theta = 0
    
    # Añadir la matriz de proyeccion
    def setProjection(self, projection):
        self.projection = projection

    def setObjective(self, GameObject):
        self.objective = GameObject

    def setAt(self, at):
        self.at = at    

    # Actualizar la matriz de vista
    def update_view(self, delta):
        if self.controller.firstPerson == True:
            at_x = self.position[0] + np.cos(self.theta)
            at_y = self.position[1] + np.sin(self.theta)
            self.eye = self.position
            self.setAt(np.array([at_x, at_y, 2]))

        if self.controller.firstPerson == False:
            self.eye = np.array([0, 0, 11])
            self.setAt(np.array([0.1, 0, 0]))
            self.up = ([0,1 ,0])

        
        # Se genera la matriz de vista
        viewMatrix = tr.lookAt(
            self.eye,
            self.at,
            self.up
        )

        self.viewMatrix = viewMatrix

    #Funcion que recibe el input para manejar la camara y controlar sus coordenadas
    def update(self, delta):
        if self.controller.firstPerson == True:
            

            # Camara se mueve adelante
            if self.controller.is_w_pressed:
                self.position += (self.at - self.position) * self.speed
                self.at += (self.at - self.position) * self.speed

            # Camara se mueve atras
            if self.controller.is_s_pressed:
                self.position -= (self.at - self.position) * self.speed
                self.at -= (self.at - self.position) * self.speed

            if self.controller.is_d_pressed:
                self.theta -= 0.05
            if self.controller.is_a_pressed:
                self.theta += 0.05

            #Strafe
            """# Camara se mueve a la izquierda  
            if self.controller.is_q_pressed:
                self.position[0] -= self.speed

            # Camara se mueve a la derecha
            if self.controller.is_e_pressed:
                self.position[0] += self.speed"""
           
        self.update_view(delta)    