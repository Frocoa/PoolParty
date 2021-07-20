from gameobject import GameObject

class Bball(GameObject):

	def __init__(self, nombre, pipeline):
		super(Bball, self).__init__(nombre, pipeline)

		self.RAD_TO_DEG = 57.2958

	
	#def update(self, delta):
	#	GameObject.update(delta)