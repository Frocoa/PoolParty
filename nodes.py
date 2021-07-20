import meshes as mh
from gameobject import GameObject
from BillardBalls import Bball
from plane3d import Plane3D
from shapes3d import *


# crea un plano con textura
def createPlane(pipeline, nombre, texture_name):
    plane = GameObject(nombre, pipeline)
    path = "assets/" + texture_name +".png"
    plane.setModel(createTextureGPUShape(createTextureNormalPlane(), pipeline, path), True)

    return plane

# crea un plano con textura que siempre mira a camara
def create3dPlane(pipeline, nombre, texture_name):
    plane = Plane3D(nombre, pipeline)
    path =  "assets/" + texture_name +".png"
    plane.setModel(createTextureGPUShape(createTextureNormalPlane(), pipeline, path), True)

    return plane

def createBillardBall(tex_pipeline, number):
    number = str(number)
    ballShape = createNormalBall(30)
    ball = Bball("bola"+ number, tex_pipeline)
    ball.setRotation([0, 90, 0])
    path = "assets/" + "b" + number + ".png"
    ball.setModel(createTextureGPUShape(ballShape, tex_pipeline, path), True)
    
    return ball

def createBalls(tex_pipeline):
    balls = []
    b1 = createBillardBall(tex_pipeline, 1)
    b1.setScale([0.52, 0.52, 0.52])
    balls.append(b1)

    b2 = createBillardBall(tex_pipeline, 2)
    b2.setScale([0.52, 0.52, 0.52])
    balls.append(b2)
    b2.setPosition([-0.52, -0.26, 0])

    b3 = createBillardBall(tex_pipeline, 3)
    b3.setScale([0.52, 0.52, 0.52])
    balls.append(b3)
    b3.setPosition([-1.04, -0.52, 0])

    b4 = createBillardBall(tex_pipeline, 4)
    b4.setScale([0.52, 0.52, 0.52])
    balls.append(b4)
    b4.setPosition([-1.56, -0.78, 0])

    b5 = createBillardBall(tex_pipeline, 5)
    b5.setScale([0.52, 0.52, 0.52])
    balls.append(b5)
    b5.setPosition([-2.08, 1.04, 0])

    b6 = createBillardBall(tex_pipeline, 6)
    b6.setScale([0.52, 0.52, 0.52])
    balls.append(b6)
    b6.setPosition([-2.08, -0.52, 0])

    b7 = createBillardBall(tex_pipeline, 7)
    b7.setScale([0.52, 0.52, 0.52])
    balls.append(b7)
    b7.setPosition([-1.56, 0.26, 0])

    b8 = createBillardBall(tex_pipeline, 8)
    b8.setScale([0.52, 0.52, 0.52])
    balls.append(b8)
    b8.setPosition([-1.04, 0, 0])

    b9 = createBillardBall(tex_pipeline, 9)
    b9.setScale([0.52, 0.52, 0.52])
    b9.setPosition([-0.52, 0.26, 0])
    balls.append(b9)

    b10 = createBillardBall(tex_pipeline, 10)
    b10.setScale([0.52, 0.52, 0.52])
    balls.append(b10)
    b10.setPosition([-1.04, 0.52, 0])

    b11 = createBillardBall(tex_pipeline, 11)
    b11.setScale([0.52, 0.52, 0.52])
    balls.append(b11)
    b11.setPosition([-1.56, 0.78, 0])

    b12 = createBillardBall(tex_pipeline, 12)
    b12.setScale([0.52, 0.52, 0.52])
    balls.append(b12)
    b12.setPosition([-2.08, -1.04, 0])

    b13 = createBillardBall(tex_pipeline, 13)
    b13.setScale([0.52, 0.52, 0.52])
    balls.append(b13)
    b13.setPosition([-2.08, 0.52, 0])

    b14 = createBillardBall(tex_pipeline, 14)
    b14.setScale([0.52, 0.52, 0.52])
    balls.append(b14)
    b14.setPosition([-1.56, -0.26, 0])

    b15 = createBillardBall(tex_pipeline, 15)
    b15.setScale([0.52, 0.52, 0.52])
    balls.append(b15)
    b15.setPosition([-2.08, 0, 0])

    cue = createBillardBall(tex_pipeline, "cue")
    cue.setScale([0.52, 0.52, 0.52])
    balls.append(cue)
    cue.setPosition([4, 0, 0])

    ballSet = GameObject("ball set", tex_pipeline)
    ballSet.addChilds(balls)

    return ballSet

def createTable(tex_pipeline):
    table = createPlane(tex_pipeline, "table", "table")
    table.setRotation([90, 90, 0])
    table.setScale([12.1, 1, 21.3 ])
    table.setPosition([0, 0, -0.26])
    return table