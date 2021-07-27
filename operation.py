import numpy as np
""" operaciones utiles"""

def normalize(v):
	norm = np.linalg.norm(v)
	if norm == 0:
		return v
	else:
		return v / norm