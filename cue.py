from gameobject import GameObject
import grafica.transformations as tr
import numpy as np

class Cue(GameObject):

	def __init__(self, nombre, pipeline, controller):
		super(Cue, self).__init__(nombre, pipeline)

		self.objective = None # Bola objetivo para el golpe
		self.controller = controller # Controlador
		self.speed = 2
		self.hitting = False
		self.canHit = True
		self.initialPos = []


	def hitBall(self, ball, strenght):
		ball.last_speed = strenght[:2]

	def update_transform(self, delta, camera):

		while self.controller.ballList[self.controller.selectedBall].inGame == False:
			self.controller.selectedBall = (self.controller.selectedBall+1) % 16

		self.objective = self.controller.ballList[self.controller.selectedBall]
		self.canHit = True

		for ball in self.controller.ballList:
			if np.linalg.norm(ball.last_speed) != 0:
				self.canHit = False

		if self.hitting == False:
			self.position = self.objective.position

			if self.controller.is_left_pressed:
				self.rotate([0, 0, self.speed])

			if self.controller.is_right_pressed:
				self.rotate([0, 0, -self.speed])

			if self.controller.is_up_pressed:
				self.childs[0].translate([0, self.speed * 0.02, 0])

			if self.controller.is_down_pressed and self.canHit:
				self.hitting = True
				self.initialPos = self.childs[0].position[1]

		elif self.canHit:
			self.childs[0].translate([0, -self.speed * 0.8, 0])

			angulo = self.rotation[2] * self.DEG_TO_RAD

			if self.childs[0].position[1] <= self.objective.radio:
				self.childs[0].position[1] = self.objective.radio

				self.hitBall(self.objective, [self.initialPos * np.sin(angulo) * 6, -self.initialPos * np.cos(angulo) * 6])
				self.hitting = False
				self.childs[0].position[1] = self.objective.radio * 2

		if self.canHit:
			GameObject.update_transform(self, delta, camera)
			angulo = self.rotation[2] * self.DEG_TO_RAD
			fuerza = np.linalg.norm([self.childs[0].position[1] * np.sin(angulo), -self.childs[0].position[1] * np.cos(angulo)])

			for ball in self.controller.ballList:
				if ball != self.objective:
					desplazamiento = [ball.position[0] - self.objective.position[0], ball.position[1] - self.objective.position[1]]

					if desplazamiento[0] != 0:
						angulo2 = np.arctan(desplazamiento[1] / desplazamiento[0])
						if desplazamiento[0] > 0:
							angulo2 = angulo2 + (180 * self.DEG_TO_RAD)
					else: angulo2 = -np.pi / 2

					ball.arrowRotation = angulo2 - (90 * self.DEG_TO_RAD)
					ball.arrowSize = np.minimum(fuerza / (np.linalg.norm(desplazamiento) * 0.4), fuerza)

				ball.canHit = True

			self.objective.arrowRotation = angulo
			self.objective.arrowSize = fuerza

		else:
		 for ball in self.controller.ballList:
		 	ball.canHit = False

	def draw(self, pipeline, transformName, camera, lights, parentTransform=tr.identity()):

		if self.canHit == True:
			GameObject.draw(self, pipeline, transformName, camera, lights, parentTransform)