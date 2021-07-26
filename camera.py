import numpy as np
import grafica.transformations as tr
import math

from operation import normalize

# Clase para manejar una camara que se mueve en coordenadas polares
class Camera:
    
    def __init__(self, controller):
        self.controller = controller
        self.at = np.array([0.0, 0.0, 2])         # donde mira la camara
        self.position = np.array([0.1, -10.0, 2]) # posicion de la camara
        self.eye = self.position                  # vector eye
        self.up = np.array([0, 0, 1])             # vector up
        self.viewMatrix = None                    # Matriz de vista
        self.projection = None                    # Matriz de proyeccion
        self.N = 1200                             # Cantidad de puntos en las curvas
        self.index = 1                            # Posicion de las curvas en las que se encuentra la camara
        self.speed = 0.15
        self.theta = np.pi/2
        self.width = 0
        self.height = 0
    
    # Añadir la matriz de proyeccion
    def setProjection(self, projection):
        self.projection = projection

    def setObjective(self, GameObject):
        self.objective = GameObject

    def setAt(self, at):
        self.at = at    

    # Actualizar la matriz de vista
    def update_view(self, delta):
        objetivo = self.controller.ballList[self.controller.selectedBall]
        for ball in self.controller.ballList:
            ball.shouldBeDrawn = True

        if self.controller.firstPerson == True:
            at_x = self.position[0] + np.cos(self.theta)
            at_y = self.position[1] + np.sin(self.theta)
            self.eye = self.position
            self.setAt(np.array([at_x, at_y, 2]))
            self.setProjection(tr.perspective(60, self.width / self.height, 0.1, 100))
            self.up = ([0, 0, 1])

        if self.controller.firstPerson == False:
            self.eye = np.array([0, 0, 20])
            self.setAt(np.array([0.1, 0, 0]))
            self.up = ([0, 1, 0])
            self.setProjection(tr.ortho(-self.width/90, self.width/90, -self.height/90, self.height/90 ,0.1, 100))

        if self.controller.canHit == False and self.controller.followBall == True and objetivo.falling == False:
            objetivo.shouldBeDrawn = False
            self.eye = np.array(objetivo.position)
            if np.linalg.norm(objetivo.last_speed) != 0:
                at = np.array([objetivo.last_speed[0], objetivo.last_speed[1], 0])
            else: at = ([1, 1, 0])

            self.setAt(self.eye + normalize(at))
            self.up = ([0, 0, 1])
            self.setProjection(tr.perspective(60, self.width / self.height, 0.1, 100))

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

            # Camara rota
            if self.controller.is_d_pressed:
                self.theta -= 0.05
            if self.controller.is_a_pressed:
                self.theta += 0.05

            #Strafe
            # Camara se mueve a la izquierda  
            if self.controller.is_q_pressed:
                self.position -= normalize(np.cross(self.at - self.position, self.up)) * self.speed
                self.at -= normalize(np.cross(self.at - self.position, self.up)) * self.speed

            # Camara se mueve a la derecha
            if self.controller.is_e_pressed:
                self.position += normalize(np.cross(self.at - self.position, self.up)) * self.speed
                self.at += normalize(np.cross(self.at - self.position, self.up)) * self.speed
           
        self.update_view(delta)    