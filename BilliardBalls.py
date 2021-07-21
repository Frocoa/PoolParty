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
		self.v0 = [0,0]
		self.h = 0.1

		self.last_speed = self.v0
		self.last_time = 0

	def f_roce(self, t, z):
		# Entrega el vector f con todas las funciones del sistema
		f = np.array([self.gravedad * self.roce * np.sign(self.last_speed[0]), self.gravedad * self.roce * np.sign(self.last_speed[1])])
		return f
	
	def addSpeed(self, speed):
		self.last_speed = [self.last_speed[0] + speed[0], self.last_speed[1] + speed[1]]

	def collide(self):
		if abs(self.position[0]) > 10.65:
			self.last_speed[0] = -self.last_speed[0]
			self.position[0] = -10.65 * np.sign(self.last_speed[0])

		if abs(self.position[1]) > 6.05:
			self.last_speed[1] = -self.last_speed[1]
			self.position[1] = -6.05 * np.sign(self.last_speed[1])

	def update_transform(self, delta, camera):
		#self.position[0] = self.last_speed[0]
		time = self.last_time + self.h
		self.last_time = time

		next_value = edo.RK4_step(self.f_roce, self.h, time, self.last_speed)
		self.last_speed = next_value

		if np.abs(self.last_speed[0]) <= 0.01:
			self.last_speed[0] = 0

		if np.abs(self.last_speed[1]) <= 0.01:
			self.last_speed[1] = 0


		self.position[0] += self.last_speed[0] * delta
		self.position[1] += self.last_speed[1] * delta

		self.rotate([-self.last_speed[1], self.last_speed[0], 0])
		self.collide()



		GameObject.update_transform(self, delta, camera)


