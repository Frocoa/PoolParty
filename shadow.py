from gameobject import GameObject
import grafica.transformations as tr
import numpy as np

class Shadow(GameObject):
	def __init__(self, nombre, pipeline):
		super(Shadow, self).__init__(nombre, pipeline)

		self.RAD_TO_DEG = 57.295779

		self.ball = None # bola a la cual esta asociado

	def update_transform(self, delta, camera):

		### Se mueve dependiendo de su posicion relativa a la luz en el centro
		if self.ball.inGame == True:
			self.setPosition([1.05 * self.ball.position[0] , 1.05 * self.ball.position[1] , -0.259])

			if self.ball.position[0] != 0:
				angulo = np.arctan(self.ball.position[1] / self.ball.position[0])
			else: angulo =  np.pi / 2

			self.setScale([0.1 * (self.ball.position[0] * np.cos(angulo) + self.ball.position[1] * np.sin(angulo)), 1, 0.5])
			self.setRotation([90, angulo * self.RAD_TO_DEG, 0])
			GameObject.update_transform(self, delta, camera)

	# Solo se dibuja si la pelota esta en juego y no cae
	def draw(self, pipeline, transformName, camera, lights, parentTransform=tr.identity()):

		if self.ball.inGame == True and self.ball.falling == False:
			GameObject.draw(self, pipeline, transformName, camera, lights, parentTransform)