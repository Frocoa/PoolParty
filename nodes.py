import meshes as mh
from gameobject import GameObject
from BilliardBalls import Bball
from cue import Cue
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

def createBilliardBall(tex_pipeline, number, posXY = [0, 0]):
    number = str(number)
    ballShape = createNormalBall(30)
    ball = Bball("bola"+ number, tex_pipeline, posXY)
    ball.setRotation([0, 90, 0])
    path = "assets/" + "b" + number + ".png"
    ball.setModel(createTextureGPUShape(ballShape, tex_pipeline, path), True)
    
    return ball

def createBalls(tex_pipeline):
    balls = []
    b1 = createBilliardBall(tex_pipeline, 1)
    b1.setScale([0.52, 0.52, 0.52])
    balls.append(b1)

    b2 = createBilliardBall(tex_pipeline, 2, [-0.52, -0.26])
    b2.setScale([0.52, 0.52, 0.52])
    balls.append(b2)

    b3 = createBilliardBall(tex_pipeline, 3, [-1.04, -0.52])
    b3.setScale([0.52, 0.52, 0.52])
    balls.append(b3)

    b4 = createBilliardBall(tex_pipeline, 4, [-1.56, -0.78])
    b4.setScale([0.52, 0.52, 0.52])
    balls.append(b4)

    b5 = createBilliardBall(tex_pipeline, 5, [-2.08, 1.04])
    b5.setScale([0.52, 0.52, 0.52])
    balls.append(b5)

    b6 = createBilliardBall(tex_pipeline, 6, [-2.08, -0.52])
    b6.setScale([0.52, 0.52, 0.52])
    balls.append(b6)

    b7 = createBilliardBall(tex_pipeline, 7, [-1.56, 0.26])
    b7.setScale([0.52, 0.52, 0.52])
    balls.append(b7)

    b8 = createBilliardBall(tex_pipeline, 8, [-1.04, 0])
    b8.setScale([0.52, 0.52, 0.52])
    balls.append(b8)

    b9 = createBilliardBall(tex_pipeline, 9, [-0.52, 0.26])
    b9.setScale([0.52, 0.52, 0.52])
    balls.append(b9)

    b10 = createBilliardBall(tex_pipeline, 10, [-1.04, 0.52])
    b10.setScale([0.52, 0.52, 0.52])
    balls.append(b10)

    b11 = createBilliardBall(tex_pipeline, 11, [-1.56, 0.78])
    b11.setScale([0.52, 0.52, 0.52])
    balls.append(b11)

    b12 = createBilliardBall(tex_pipeline, 12, [-2.08, -1.04])
    b12.setScale([0.52, 0.52, 0.52])
    balls.append(b12)

    b13 = createBilliardBall(tex_pipeline, 13, [-2.08, 0.52])
    b13.setScale([0.52, 0.52, 0.52])
    balls.append(b13)

    b14 = createBilliardBall(tex_pipeline, 14, [-1.56, -0.26])
    b14.setScale([0.52, 0.52, 0.52])
    balls.append(b14)

    b15 = createBilliardBall(tex_pipeline, 15, [-2.08, 0])
    b15.setScale([0.52, 0.52, 0.52])
    balls.append(b15)

    bcue = createBilliardBall(tex_pipeline, "cue", [4, 0])
    bcue.setScale([0.52, 0.52, 0.52])
    balls.append(bcue)

    ballSet = GameObject("ball set", tex_pipeline)
    ballSet.addChilds(balls)

    for ball in balls:
        auxList = balls[:]
        auxList.remove(ball)
        ball.collBalls = auxList


    return ballSet

def createCue(pipeline, controller):
    cueMesh = mh.createCueMesh()
    cueShape = createGPUShape(pipeline, mh.toShape(cueMesh, color=(255/255, 128/255, 0.0)))

    cueModel = GameObject("cue model", pipeline)
    cueModel.setModel(cueShape)
    cueModel.setRotation([90, 0, 0])
    cueModel.setScale([0.6, 0.6, 10])
    cueModel.setPosition([0, 1, 0])

    cueCenter = Cue("cue", pipeline, controller)
    cueCenter.addChilds([cueModel])
    cueCenter.setPosition([4, 0, 0])
    cueCenter.setRotation([0, 0, 0])
    
    return cueCenter

def createTable(tex_pipeline):
    table = createPlane(tex_pipeline, "table", "table")
    table.setRotation([90, 90, 0])
    table.setScale([12.1, 1, 21.3 ])
    table.setPosition([0, 0, -0.26])
    return table