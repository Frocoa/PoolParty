""" Al final no use esta clase """

from plane3d import Plane3D
import numpy as np

class HudPlane(Plane3D):

	def __init__(self, nombre, pipeline):
		super(HudPlane, self).__init__(nombre, pipeline)

		self.screenPos = np.array([0, 5, 0])
		# y es que tan lejos de la camara esta
		# x, z es la posicion en la ventana

	def update_transform(self, delta, camera):

		# se mantiene siempre en el mismo punto relativo a la camara

		if (camera.at[0]) != 0:
			angulo = np.arctan((camera.at[1] - camera.position[1])/(camera.at[0] - camera.position[0]))
		else:
			angulo = (np.pi / 2)

		x = camera.position[0] + self.screenPos[1] * np.cos(angulo)
		y = camera.position[1] + self.screenPos[1] * np.sin(angulo)

		self.setPosition(np.array([x, y, self.position[2]]))

		Plane3D.update_transform(self, delta, camera)