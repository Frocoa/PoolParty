import openmesh
import math
import numpy as np
import grafica.basic_shapes as bs

def createCueMesh(textured=False):

	mesh = openmesh.TriMesh()

	# abajo
	d1 = mesh.add_vertex(np.array([  0.5,   0.0,  -1.0]))
	d2 = mesh.add_vertex(np.array([ 0.25, -0.433, -1.0]))
	d3 = mesh.add_vertex(np.array([-0.25, -0.433, -1.0]))
	d4 = mesh.add_vertex(np.array([ -0.5,    0.0, -1.0]))
	d5 = mesh.add_vertex(np.array([-0.25,  0.433, -1.0]))
	d6 = mesh.add_vertex(np.array([ 0.25,  0.433, -1.0])) 

	# arriba
	u1 = mesh.add_vertex(np.array([  0.3,   0.0,  0.0]))
	u2 = mesh.add_vertex(np.array([ 0.15, -0.259, 0.0]))
	u3 = mesh.add_vertex(np.array([-0.15, -0.259, 0.0]))
	u4 = mesh.add_vertex(np.array([ -0.3,    0.0, 0.0]))
	u5 = mesh.add_vertex(np.array([-0.15,  0.259, 0.0]))
	u6 = mesh.add_vertex(np.array([ 0.15,  0.259, 0.0])) 

	# tapa de abajo
	mesh.add_face([d2, d3 ,d1])
	mesh.add_face([d1, d3, d4])
	mesh.add_face([d1, d4, d6])
	mesh.add_face([d6, d4, d5])

	# laterales
	mesh.add_face([d1, u1, u2])
	mesh.add_face([u2, d2, d1])

	mesh.add_face([d2, u2, u3])
	mesh.add_face([u3, d3, d2])

	mesh.add_face([d3, u3, u4])
	mesh.add_face([u4, d4, d3])

	mesh.add_face([d4, u4, u5])
	mesh.add_face([u5, d5, d4])

	mesh.add_face([d5, u5, u6])
	mesh.add_face([u6, d6, d5])

	mesh.add_face([d6, u6, u1])
	mesh.add_face([u1, d1, d6])

	# tapa de arriba
	mesh.add_face([u3, u2, u1])
	mesh.add_face([u3, u1, u4])
	mesh.add_face([u4, u1, u6])
	mesh.add_face([u4, u6, u5])

	return mesh

def createAmortiguador(textured = False):

	mesh = openmesh.TriMesh()

	# abajo
	d1 = mesh.add_vertex(np.array([  -0.5,  0.5,  -0.5]))
	d2 = mesh.add_vertex(np.array([  -0.43, -0.5,  -0.5]))
	d3 = mesh.add_vertex(np.array([  0.43,   -0.5,  -0.5]))
	d4 = mesh.add_vertex(np.array([  0.5,   0.5,  -0.5]))

	# arriba
	u1 = mesh.add_vertex(np.array([  -0.5,  0.5,  0.5]))
	u2 = mesh.add_vertex(np.array([  -0.44, -0.5,  0.5]))
	u3 = mesh.add_vertex(np.array([  0.44,   -0.5,  0.5]))
	u4 = mesh.add_vertex(np.array([  0.5,   0.5,  0.5]))

	# tapa de abajo
	mesh.add_face([d3, d2 ,d1])
	mesh.add_face([d4, d3, d1])

	# laterales
	mesh.add_face([d1, d2, u2])
	mesh.add_face([d1, u2, u1])

	mesh.add_face([d2, d3, u3])
	mesh.add_face([d2, u3, u2])

	mesh.add_face([d3, d4, u4])
	mesh.add_face([d3, u4, u3])

	mesh.add_face([d4, d1, u1])
	mesh.add_face([d4, u1, u4])

	# tapa de arriba
	mesh.add_face([u1, u2, u3])
	mesh.add_face([u3, u4, u1])

	return mesh

def toShape(mesh, color=None, textured=False, verbose=False):
    assert isinstance(mesh, openmesh.TriMesh)
    assert (color != None) != textured, "The mesh will be colored or textured, only one of these need to be specified."

    # Requesting normals per face
    mesh.request_face_normals()

    # Requesting normals per vertex
    mesh.request_vertex_normals()

    # Computing all requested normals
    mesh.update_normals()

    # You can also update specific normals
    #mesh.update_face_normals()
    #mesh.update_vertex_normals()
    #mesh.update_halfedge_normals()

    # At this point, we are sure we have normals computed for each face.
    assert mesh.has_face_normals()

    vertices = []
    indices = []

    # To understand how iteraors and circulators works in OpenMesh, check the documentation at:
    # https://www.graphics.rwth-aachen.de:9000/OpenMesh/openmesh-python/-/blob/master/docs/iterators.rst

    def extractCoordinates(numpyVector3):
        assert len(numpyVector3) == 3
        x = vertex[0]
        y = vertex[1]
        z = vertex[2]
        return [x,y,z]

    # This is inefficient, but it works!
    # You can always optimize it further :)

    # Checking each face
    for faceIt in mesh.faces():
        faceId = faceIt.idx()
        if verbose: print("face: ", faceId)

        # Checking each vertex of the face
        for faceVertexIt in mesh.fv(faceIt):
            faceVertexId = faceVertexIt.idx()

            # Obtaining the position and normal of each vertex
            vertex = mesh.point(faceVertexIt)
            normal = mesh.normal(faceVertexIt)
            if verbose: print("vertex ", faceVertexId, "-> position: ", vertex, " normal: ", normal)

            x, y, z = extractCoordinates(vertex)
            nx, ny, nz = extractCoordinates(normal)

            if textured:
                assert mesh.has_vertex_texcoords2D()

                texcoords = mesh.texcoord2D(faceVertexIt)
                tx = texcoords[0]
                ty = texcoords[1]
                
                vertices += [x, y, z, tx, ty, nx, ny, nz]
                indices += [len(vertices)//8 - 1]
            else:
                assert color != None

                r = color[0]
                g = color[1]
                b = color[2]

                vertices += [x, y, z, r, g, b, nx, ny, nz]
                indices += [len(vertices)//9 - 1]
        
        if verbose: print()

    return bs.Shape(vertices, indices)    