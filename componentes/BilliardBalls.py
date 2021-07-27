from gameobject import GameObject
import numpy as np
import ode_resolver as edo
import grafica.transformations as tr

class Bball(GameObject):

	def __init__(self, nombre, pipeline, posXY, indice, controller):
		super(Bball, self).__init__(nombre, pipeline)

		self.RAD_TO_DEG = 57.2958

		self.position = [posXY[0], posXY[1], 0] 	# Posicion
		self.controller = controller            	# Referencia al controlador
		self.indice = indice                    	# Indice personal
		self.radio = 0.26                       	# Radio de la pelota

		self.inGame = True                      	# La bola sigue en juego
		self.falling = False                    	# La bola esta cayendo a un bolsillo
		self.canHit = False                         # La bola puede ser golpeada
		self.shouldBeDrawn = True               	# La bola deberia ser dibujada

		self.Ks = [0.05, 0.05, 0.05]            	# Coeficiente especular
		self.shininess = 70;                    	# Brillo

		self.roce = self.controller.roce            # Coeficiente de roce
		self.c_r_bola = self.controller.restitucion # Coeficiente de restitucion
		self.c_r_muralla = 0.99                     # Coeficiente de restitucion con la muralla

		self.arrowRotation = 0                      # Rotacion de los vectores
		self.arrowSize = 0                          # Tamaño de los vectores

		self.gravedad = -9.8                    	# Gravedad
		self.v0 = [0, 0]                        	# Velocidad incial
		self.vCaida = [0]                       	# Velocidad de caida
		self.h = 0.1                            	# Intervalos para la EDO
		self.last_speed = self.v0                   # Velocidad en el frame anterior
		self.last_speedF = self.vCaida              # Velocidad de caida en el frame anterior
		self.last_time = 0                          # last time para la EDO
		self.fallingCoords = [0, 0]                 # Coordenadas del bolsillo donde cayo la bola

		self.collBalls = []                     	# Lista de las otras pelotas para colisionar
		self.alreadyCollided = None                 # Pelota con la que ya se colisiono
		self.collideFrames = 0                      # Tiempo antes de poder volver chocar con la misma bola

	def f_roce(self, t, z):
		# Entrega el vector f con todas las funciones del sistema
		# se multiplica por la velocidad porque, aunque no sea muy realista, ayuda a evitar
		# que se terminen moviendo en un solo eje y asi queda mejor
		f = np.array([self.gravedad * self.roce * self.last_speed[0],\
					 self.gravedad * self.roce * self.last_speed[1]]) 
		return f
	
	# Funcion con la fisica de caida en un bolsillo de la pelota
	def f_caida(self, t, z):
		f = np.array([self.gravedad])
		return f

	# Agregar velocidad
	def addSpeed(self, speed):
		self.last_speed = [self.last_speed[0] + speed[0], self.last_speed[1] + speed[1]]

	# Caer en un bolsillo
	def holeCollide(self):
		holePos = [[0, -6.1], [0, 6.1], [12.5, 6.1], [-12.5, 6.1], [12.5, -6.1], [-12.5, -6.1]]
		for coords in holePos:
			magnitud = np.linalg.norm([coords[0] - self.position[0], coords[1] - self.position[1]])
			if magnitud <= (0.75): #ligeramente mas grande que el agujero real
				self.falling = True
				self.fallingCoords = coords

	# Chocar con una muralla
	def wallCollide(self):
		if abs(self.position[0]) > 12.43:
			self.last_speed[0] = -self.last_speed[0] * self.c_r_muralla
			self.position[0] = -12.43 * np.sign(self.last_speed[0])

		if abs(self.position[1]) > 5.9:
			self.last_speed[1] = -self.last_speed[1] * self.c_r_muralla
			self.position[1] = -5.9 * np.sign(self.last_speed[1])

	# Chocar con otra pelota
	def ballCollide(self):
		for ball in self.collBalls:
			if ball.inGame == True:
				magnitud = np.linalg.norm([ball.position[0] - self.position[0], ball.position[1] - self.position[1]])

				# Choque con una bola
				if magnitud < (self.radio + ball.radio):

					if (ball == self.alreadyCollided and self.collideFrames > 10) or ball != self.alreadyCollided:
						self.bounce(ball)
						self.alreadyCollided = ball
						self.collideFrames = 0
						ball.alreadyCollided = self
						ball.collideFrames = 0

				# Evitar que hagan clipping
				if magnitud < (self.radio + ball.radio):	
					d = (self.radio + ball.radio) - magnitud
					if (ball.position[0] - self.position[0]) != 0: 
						angulo = np.arctan( (ball.position[1] - self.position[1]) / (ball.position[0] - self.position[0]))

					else: angulo = np.pi / 2
					self.position[0] += d * np.cos(angulo)
					self.position[1] += d * np.sin(angulo)
				
	# Fisica del rebote con una pelota
	def bounce(self, col):
			pos_1, pos_2 = np.array(self.position[:2]), np.array(col.position[:2])

			distancia = np.linalg.norm(pos_1 - pos_2) ** 2

			vi_1 , vi_2 = np.array(self.last_speed), np.array(col.last_speed)
			vf_1 = vi_1 - np.dot(vi_1 - vi_2, pos_1 - pos_2) / distancia * (pos_1 - pos_2)
			vf_2 = vi_2 - np.dot(vi_2 - vi_1, pos_2 - pos_1) / distancia * (pos_2 - pos_1)

			self.last_speed = vf_1 * self.c_r_bola
			col.last_speed = vf_2 * col.c_r_bola

	# Soobrescibe el update_transform
	def update_transform(self, delta, camera):

		if self.inGame == True and self.falling == False:
			self.ballCollide()
			self.wallCollide()
			self.holeCollide()
			self.canHit = self.controller.canHit
			tecnica = self.controller.indice_tecnica
			self.collideFrames += 1

			time = self.last_time + self.h * delta
			self.last_time = time

			### Elegir tecnica de resolucion de EDO
			if tecnica == 0:
				next_value = edo.RK4_step(self.f_roce, self.h, time, self.last_speed)
			elif tecnica == 1:
				next_value = edo.euler_step(self.f_roce, self.h, time, self.last_speed)
			elif tecnica == 2:
				next_value = edo.euler_mejorado_step(self.f_roce, self.h, time, self.last_speed)
			elif tecnica == 3:
				next_value = edo.euler_modificado_step(self.f_roce, self.h, time, self.last_speed)

			self.last_speed = next_value

			# Si la bola va muy lento, se aproxima a 0
			if np.abs(np.linalg.norm(self.last_speed)) <= 0.3:
				self.last_speed = np.array([0, 0])

			# Se mueve y rota segun su velocidad
			self.translate([self.last_speed[0] * delta, self.last_speed[1] * delta, 0])
			self.rotate([-self.last_speed[1]/self.radio, self.last_speed[0]/self.radio, 0])

		# La pelota cae por un bolsillo
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

		# La pelota ya cayo y esta fuera del juego
		elif self.inGame == False:
			self.setPosition([2 + self.indice*0.53, 6.5, 0.52]) # Se mueve al borde de la mes
			self.setRotation([0, 0, 90])
			self.last_speed = ([0, 0, 0])

		GameObject.update_transform(self, delta, camera)

	# Se dibuja solo si deberia ser dibujada
	def draw(self, pipeline, transformName, camera, lights, parentTransform=tr.identity()):

		if self.shouldBeDrawn == True:
			GameObject.draw(self, pipeline, transformName, camera, lights, parentTransform)


