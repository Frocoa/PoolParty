from gameobject import GameObject, findGameObject
import numpy as np
import grafica.transformations as tr

""" Vectores de fuerza """
class Trayectoria(GameObject):

	def __init__(self, nombre, pipeline):
		super(Trayectoria, self).__init__(nombre, pipeline)

		self.ball = None 			# bola a la cual esta asociado
		self.RAD_TO_DEG = 57.295779

	def update_transform(self, delta, camera):
		angulo = self.ball.arrowRotation
		self.setPosition([self.ball.position[0] + 0.2 * self.ball.arrowSize * np.sin(angulo) \
						, self.ball.position[1] - 0.2 * self.ball.arrowSize * np.cos(angulo) , -0.258])

		self.setScale([0.5, 1, 0.4 * self.ball.arrowSize])
		self.setRotation([90, angulo * self.RAD_TO_DEG, 0])

		GameObject.update_transform(self, delta, camera)

	# Se dibuja solo si esta en juego y el taco puede golpear
	def draw(self, pipeline, transformName, camera, lights, parentTransform=tr.identity()):

		if self.ball.canHit == True and self.ball.inGame == True:
			GameObject.draw(self, pipeline, transformName, camera, lights, parentTransform)