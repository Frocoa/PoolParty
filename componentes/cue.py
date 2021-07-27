from gameobject import GameObject
import grafica.transformations as tr
import numpy as np

class Cue(GameObject):

	def __init__(self, nombre, pipeline, controller):
		super(Cue, self).__init__(nombre, pipeline)

		self.objective = None 		 # bola objetivo para el golpe
		self.controller = controller # referencia l controlador
		self.speed = 2               # velocidad del taco
		self.hitting = False         # esta golpeando
		self.initialPos = []         # posicion inicial antes del golpe


	# Golpear el objetivo
	def hitBall(self, ball, strenght):
		ball.last_speed = strenght[:2]

	# Sobreescribir el transform
	def update_transform(self, delta, camera):

		# Si la bola seleccionada ya no esta en juego, se va a la siguiente
		while self.controller.ballList[self.controller.selectedBall].inGame == False:
			self.controller.selectedBall = (self.controller.selectedBall+1) % 16

		self.objective = self.controller.ballList[self.controller.selectedBall]
		self.controller.canHit = True

		for ball in self.controller.ballList:
			if np.linalg.norm(ball.last_speed) != 0:
				self.controller.canHit = False

		### El taco esta posicionandose
		if self.hitting == False:
			self.position = self.objective.position # se mueve a su objetivo

			## Movimiento del taco
			if self.controller.is_left_pressed:
				self.rotate([0, 0, self.speed])

			if self.controller.is_right_pressed:
				self.rotate([0, 0, -self.speed])

			if self.controller.is_up_pressed:
				self.childs[0].translate([0, self.speed * 0.02, 0])

			if self.controller.is_down_pressed:
				self.childs[0].translate([0, -self.speed * 0.02, 0])

			# El taco decide golpear
			if self.controller.is_space_pressed and self.controller.canHit:
				self.hitting = True
				self.initialPos = self.childs[0].position[1]

			# Limite en el movimiento del taco
			if self.childs[0].position[1] <= self.objective.radio:
				self.childs[0].position[1] = self.objective.radio

			if self.childs[0].position[1] >= self.objective.radio * 30:
				self.childs[0].position[1] = self.objective.radio * 30

		### El taco esta golpeando
		elif self.controller.canHit:
			self.childs[0].translate([0, -self.speed * 0.4 , 0]) # se acerca al objetivo rapido

			angulo = self.rotation[2] * self.DEG_TO_RAD

			## Golpe a la pelota
			if self.childs[0].position[1] <= self.objective.radio:
				self.childs[0].position[1] = self.objective.radio

				self.hitBall(self.objective, [self.initialPos * np.sin(angulo) * 6, -self.initialPos * np.cos(angulo) * 6])
				self.hitting = False
				self.childs[0].position[1] = self.objective.radio * 2

		### Mientras el taco se carga
		if self.controller.canHit:
			GameObject.update_transform(self, delta, camera)

			## Se maneja el vector de fuerza de todas las bolas de la mesa
			angulo = self.rotation[2] * self.DEG_TO_RAD
			fuerza = np.linalg.norm([self.childs[0].position[1] * np.sin(angulo), -self.childs[0].position[1] * np.cos(angulo)])
			self.controller.fuerza = fuerza

			# todas las bolas de la mesa
			for ball in self.controller.ballList:
				if ball != self.objective:
					desplazamiento = [ball.position[0] - self.objective.position[0], ball.position[1] - self.objective.position[1]]

					if desplazamiento[0] != 0:
						angulo2 = np.arctan(desplazamiento[1] / desplazamiento[0])
						if desplazamiento[0] > 0:
							angulo2 = angulo2 + (180 * self.DEG_TO_RAD)
					else: angulo2 = -np.pi / 2

					ball.arrowRotation = angulo2 - (90 * self.DEG_TO_RAD)
					ball.arrowSize = np.minimum(fuerza / (np.linalg.norm(desplazamiento) * 0.25), fuerza) # potencia depende de la distancia

			# bola objetivo
			self.objective.arrowRotation = angulo
			self.objective.arrowSize = fuerza
		
		else:
		 for ball in self.controller.ballList:
		 	ball.controller.canHit = False

	# Solo se debe dibujar el taco cuando todo este quieto
	def draw(self, pipeline, transformName, camera, lights, parentTransform=tr.identity()):

		if self.controller.canHit == True:
			GameObject.draw(self, pipeline, transformName, camera, lights, parentTransform)