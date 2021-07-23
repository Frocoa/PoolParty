from gameobject import GameObject
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

			if self.childs[0].position[1] <= self.objective.radio:
				self.childs[0].position[1] = self.objective.radio

				angulo = self.rotation[2] * self.DEG_TO_RAD
				self.hitBall(self.objective, [self.initialPos * np.sin(angulo) * 6, -self.initialPos * np.cos(angulo) * 6])
				self.hitting = False
				self.childs[0].position[1] = self.objective.radio * 2

		#self.childs[0]
		if self.canHit:
			GameObject.update_transform(self, delta, camera)