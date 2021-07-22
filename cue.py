from gameobject import GameObject

class Cue(GameObject):

	def __init__(self, nombre, pipeline, controller):
		super(Cue, self).__init__(nombre, pipeline)
		self.objective = None # Bola objetivo para el golpe

	def update_transform(self, delta, camera):
		#self.childs[0]
		GameObject.update_transform(self, delta, camera)