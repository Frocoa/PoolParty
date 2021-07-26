from plane3d import Plane3D
from OpenGL.GL import *
import grafica.transformations as tr
import numpy as np

""" Al final por como lo hice no tiene necesidad de ser un Plane3D, pero no pierde nada por serlo"""
class Bar(Plane3D):
	def __init__(self, nombre, pipeline, controller, outline):
		super(Bar, self).__init__(nombre, pipeline)

		self.texturas = [] # Las 2 texturas de la barra
		self.charge = 70.0 # Que tan cargada esta la barra entre 0 y 100
		self.controller = controller # referencia al controlador
		self.theta = 1 # velocidad del efecto de shearing
		self.outline = outline # referencia al borde
		self.v0 = 0 # velocidad inicial del efecto

	def tambalear(self):
		self.currentFrames += 1
		self.transform = tr.matmul([
				tr.translate(self.position[0], self.position[1], self.position[2]),

				# las rotaciones siempre van a ser en orden x,y,z
				tr.rotationX(self.rotation[0] * self.DEG_TO_RAD),
				tr.rotationY(self.rotation[1] * self.DEG_TO_RAD),
            	tr.rotationZ(self.rotation[2] * self.DEG_TO_RAD),
            	tr.scale(self.scale[0], self.scale[1], self.scale[2]),
            	tr.shearing(0, 0, 0, np.cos(self.v0 * 1.3 /(self.theta**2)), 0, 0)
			])

		self.outline.transform = tr.matmul([
				tr.translate(self.position[0], self.position[1], self.position[2]),

				# las rotaciones siempre van a ser en orden x,y,z
				tr.rotationX(self.rotation[0] * self.DEG_TO_RAD),
				tr.rotationY(self.rotation[1] * self.DEG_TO_RAD),
            	tr.rotationZ(self.rotation[2] * self.DEG_TO_RAD),
            	tr.scale(self.scale[0], self.scale[1], self.scale[2]),
            	tr.shearing(0, 0, 0, np.cos(self.v0 * 1.3/(self.theta**2)), 0, 0)
			])

	def update_transform(self, delta, camera):

		Plane3D.update_transform(self, delta, camera)

		if self.controller.tambalear == True and self.controller.canHit == True:
			self.tambalear()
			self.theta += 8 * self.DEG_TO_RAD
		else:
			self.controller.tambalear = False
			self.currentFrames = 0
			self.theta = 1
			self.v0 = self.controller.fuerza

			

	


	def draw(self, pipeline, transformName, camera, lights, parentTransform=tr.identity()):

		glUseProgram(self.pipeline.shaderProgram)

		# Se manda cuanta carga hay en la barra
		#       #rango de los pixeles	  #rango de la fuerza							#inicio de los pixeles
		carga = (145) 					/ ((7.54) 			/ self.controller.fuerza) + 70

		glUniform1f(glGetUniformLocation(pipeline.shaderProgram, "charge"), carga)

		Plane3D.draw(self, pipeline, transformName, camera, lights, parentTransform)