from gameobject import GameObject

class Cue(GameObject):

	def __init__(self, nombre, pipeline, controller):
		super(Cue, self).__init__(nombre, pipeline)
		self.objective = None # Bola objetivo para el golpe
		self.controller = controller # Controlador
		self.speed = 2

	def update_transform(self, delta, camera):
		if self.controller.is_left_pressed:
			self.rotate([0, 0, self.speed])

		if self.controller.is_right_pressed:
			self.rotate([0, 0, -self.speed])

		if self.controller.is_up_pressed:
			self.childs[0].translate([0, self.speed * 0.2, 0])

		if self.controller.is_down_pressed:
			self.childs[0].translate([0, -self.speed * 0.2, 0])

		#self.childs[0]
		GameObject.update_transform(self, delta, camera)