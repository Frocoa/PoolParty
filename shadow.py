from gameobject import GameObject
import numpy as np

class Shadow(GameObject):
	def __init__(self, nombre, pipeline):
		super(Shadow, self).__init__(nombre, pipeline)

		self.RAD_TO_DEG = 57.295779

		self.ball = None

	def update_transform(self, delta, camera):
		self.setPosition([1.1 * self.ball.position[0] , 1.1 * self.ball.position[1] , -0.259])
		if self.ball.position[0] != 0:
			angulo = np.arctan(self.ball.position[1] / self.ball.position[0])
		else: angulo =  np.pi / 2

		self.setScale([0.2 * (self.ball.position[0] * np.cos(angulo) + self.ball.position[1] * np.sin(angulo)), 1, 0.5])
		self.setRotation([90, angulo * self.RAD_TO_DEG, 0])
		GameObject.update_transform(self, delta, camera)
