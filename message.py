from plane3d import Plane3D

class Message(Plane3D):
	def __init__(self, nombre, pipeline, controller):
		super(Message, self).__init__(nombre, pipeline)
		self.modelos = []
		self.controller = controller

	def addModels(self, modelos):
		self.modelos += modelos

	def update_transform(self, delta, camera):
		modeloActual = self.modelos[self.controller.indice_tecnica]
		self.setModel(modeloActual)

		if self.controller.firstPerson == True:
			self.setPosition([0, 0, 4])
			self.rotation[0] , self.rotation[1] = 0, 0
			self.setScale([10, 10, 10])

		else:
			self.setPosition([0, 8, 10])
			self.setRotation([90, 180, 0])
			self.setScale([5, 5, 5])

		Plane3D.update_transform(self, delta, camera)