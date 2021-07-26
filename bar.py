from plane3d import Plane3D
from OpenGL.GL import *
import grafica.transformations as tr

""" Al final por como lo hice no tiene necesidad de ser un Plane3D, pero no pierde nada por serlo"""
class Bar(Plane3D):
	def __init__(self, nombre, pipeline, controller):
		super(Bar, self).__init__(nombre, pipeline)

		self.texturas = [] # Las 2 texturas de la barra
		self.charge = 70.0 # Que tan cargada esta la barra entre 0 y 100
		self.controller = controller # referencia al controlador

	def update_transform(self, delta, camera):

		Plane3D.update_transform(self, delta, camera)

	def draw(self, pipeline, transformName, camera, lights, parentTransform=tr.identity()):

		glUseProgram(self.pipeline.shaderProgram)

		# Se manda cuanta carga hay en la barra
		#       #rango de los pixeles	  #rango de la fuerza							#inicio de los pixeles
		carga = (145) 					/ ((7.54) 			/ self.controller.fuerza) + 70

		glUniform1f(glGetUniformLocation(pipeline.shaderProgram, "charge"), carga)

		Plane3D.draw(self, pipeline, transformName, camera, lights, parentTransform)