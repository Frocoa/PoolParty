from gameobject import GameObject
import numpy as np
import ode_resolver as edo

class Bball(GameObject):

	def __init__(self, nombre, pipeline, posXY, indice):
		super(Bball, self).__init__(nombre, pipeline)

		self.RAD_TO_DEG = 57.2958
		self.position = [posXY[0], posXY[1], 0]
		self.indice = indice
		self.roce = 0.01
		self.gravedad = -9.8
		self.v0 = [0, 0]
		self.vCaida = [0]
		self.h = 0.1
		self.radio = 0.26
		self.collBalls = []
		self.inGame = True
		self.falling = False

		self.c_r_bola = 0.95
		self.c_r_muralla = 0.99

		self.arrowRotation = 0
		self.arrowSize = 0
		self.canHit = False

		self.last_speed = self.v0
		self.last_speedF = self.vCaida
		self.last_time = 0

		self.alreadyCollided = None
		self.collideFrames = 0

		self.fallingCoords = [0, 0]

	def f_roce(self, t, z):
		# Entrega el vector f con todas las funciones del sistema
		# se multiplica por la velocidad porque, aunque no sea muy realista, ayuda a evitar
		# que se terminen moviendo en un solo eje y asi queda mejor
		f = np.array([self.gravedad * self.roce * self.last_speed[0],\
					 self.gravedad * self.roce * self.last_speed[1]]) 
		return f
	
	def f_caida(self, t, z):
		f = np.array([self.gravedad])
		return f

	def addSpeed(self, speed):
		self.last_speed = [self.last_speed[0] + speed[0], self.last_speed[1] + speed[1]]

	def holeCollide(self):
		holePos = [[0, -6.1], [0, 6.1], [12.5, 6.1], [-12.5, 6.1], [12.5, -6.1], [-12.5, -6.1]]
		for hole in holePos:
			magnitud = np.linalg.norm([hole[0] - self.position[0], hole[1] - self.position[1]])
			if magnitud <= (self.radio + 0.6):
				self.falling = True
				self.fallingCoords = hole

	def wallCollide(self):
		if abs(self.position[0]) > 12.43:
			self.last_speed[0] = -self.last_speed[0] * self.c_r_muralla
			self.position[0] = -12.43 * np.sign(self.last_speed[0])

		if abs(self.position[1]) > 5.9:
			self.last_speed[1] = -self.last_speed[1] * self.c_r_muralla
			self.position[1] = -5.9 * np.sign(self.last_speed[1])

	def ballCollide(self):
		for ball in self.collBalls:
			if ball.inGame == True:
				magnitud = np.linalg.norm([ball.position[0] - self.position[0], ball.position[1] - self.position[1]])

				if magnitud <= (self.radio + ball.radio):

					if (ball == self.alreadyCollided and self.collideFrames > 10) or ball != self.alreadyCollided:
						self.bounce(ball)
						self.alreadyCollided = ball
						self.collideFrames = 0
						ball.alreadyCollided = self
						ball.collideFrames = 0

				if magnitud < (self.radio + ball.radio):	
					d = (self.radio + ball.radio) - magnitud
					if (ball.position[0] - self.position[0]) != 0: 
						angulo = np.arctan( (ball.position[1] - self.position[1]) / (ball.position[0] - self.position[0]))

					else: angulo = np.pi / 2
					self.position[0] += d * np.cos(angulo)
					self.position[1] += d * np.sin(angulo)
				

	def bounce(self, col):
			r1, r2 = np.array(self.position[:2]), np.array(col.position[:2])

			d = np.linalg.norm(r1 - r2) ** 2

			v1 , v2 = np.array(self.last_speed), np.array(col.last_speed)
			u1 = v1 - np.dot(v1 - v2, r1 - r2) / d * (r1 - r2)
			u2 = v2 - np.dot(v2 - v1, r2 - r1) / d * (r2 - r1)

			self.last_speed = u1 * self.c_r_bola
			col.last_speed = u2 * col.c_r_bola

	def update_transform(self, delta, camera):

		if self.inGame == True and self.falling == False:
			self.ballCollide()
			self.wallCollide()
			self.holeCollide()

			self.collideFrames += 1

			time = self.last_time + self.h * delta
			self.last_time = time
			next_value = edo.RK4_step(self.f_roce, self.h, time, self.last_speed)
			self.last_speed = next_value

			if np.abs(np.linalg.norm(self.last_speed)) <= 0.3:
				self.last_speed = np.array([0, 0])

			self.translate([self.last_speed[0] * delta, self.last_speed[1] * delta, 0])
			self.rotate([-self.last_speed[1]/self.radio, self.last_speed[0]/self.radio, 0])

		elif self.falling == True:
			time = self.last_time + self.h * delta
			self.last_time = time
			next_value = edo.RK4_step(self.f_caida, self.h, time, self.last_speedF)
			self.last_speedF = next_value

			self.setPosition([self.fallingCoords[0], self.fallingCoords[1], self.position[2]])
			self.translate([0, 0, self.last_speedF * 0.1 * delta])

			if self.position[2] <= -0.56:
				self.falling = False
				self.inGame = False

		elif self.inGame == False:
			self.setPosition([2 + self.indice*0.53, 6.2, 0.52])
			self.setRotation([0, 0, 90])
			self.last_speed = ([0, 0, 0])

		GameObject.update_transform(self, delta, camera)


