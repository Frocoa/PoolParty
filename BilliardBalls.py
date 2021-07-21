from gameobject import GameObject
import numpy as np
import ode_resolver as edo

class Bball(GameObject):

	def __init__(self, nombre, pipeline, posXY):
		super(Bball, self).__init__(nombre, pipeline)

		self.RAD_TO_DEG = 57.2958
		self.position = [posXY[0], posXY[1], 0]
		self.roce = 0.06
		self.gravedad = -9.8
		self.v0 = [4,4]
		self.h = 0.1

		self.last_z = self.v0
		self.last_time = 0

	def f_roce(self, t, z):
		# Entrega el vector f con todas las funciones del sistema
		f = np.array([self.gravedad * self.roce, self.gravedad * self.roce])
		return f
	
	def update_transform(self, delta, camera):
		#self.position[0] = self.last_z[0]
		time = self.last_time + self.h
		self.last_time = time

		next_value = edo.RK4_step(self.f_roce, self.h, time, self.last_z)
		self.last_z = next_value

		if np.abs(np.linalg.norm(self.last_z)) <= 0.1:
			self.last_z = [0, 0]

		print(self.last_z)
		self.position[0] += self.last_z[0] * delta
		self.position[1] += self.last_z[1] * delta




		GameObject.update_transform(self, delta, camera)


