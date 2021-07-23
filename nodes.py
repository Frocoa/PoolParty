import meshes as mh
from gameobject import GameObject
from BilliardBalls import Bball
from shadow import Shadow
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
    ballModel = GameObject("bola"+ number + "model", tex_pipeline)
    ballModel.setRotation([0, 90, 0])
    path = "assets/" + "b" + number + ".png"
    ballModel.setModel(createTextureGPUShape(ballShape, tex_pipeline, path), True)

    ball = Bball("bola" + number, tex_pipeline, posXY, int(number))
    ball.addChilds([ballModel])

    return ball


def createBalls(tex_pipeline):
    shadowPath = "assets/shadow.png"

    balls = []
    shadows = []
    b1 = createBilliardBall(tex_pipeline, 1)
    b1.setScale([0.52, 0.52, 0.52])
    b1.setRotation([0, 25, 0])
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

    bcue = createBilliardBall(tex_pipeline, 0, [4, 0])
    bcue.setScale([0.52, 0.52, 0.52])
    balls.append(bcue)

    ballSet = GameObject("ball set", tex_pipeline)
    ballSet.addChilds(balls)
    

    for ball in balls:
        auxList = balls[:]
        auxList.remove(ball)
        ball.collBalls = auxList

    for ball in balls:
        shadow = Shadow("sombra", tex_pipeline)
        shadow.ball = ball
        shadow.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, shadowPath), True)
        shadow.setRotation([90, 0, 0])
        shadows.append(shadow)

    ballSet.addChilds(shadows)

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

def createTable(pipeline, tex_pipeline):

    holePath = "assets/shadow.png"

    holeModel = GameObject("hole", tex_pipeline)
    holeModel.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, holePath), True)
    holeModel.setRotation([90, 0, 0])
    holeModel.setPosition([0, 0, -0.259])

    tableMesh = mh.createAmortiguador()
    tableShape = createGPUShape(pipeline, mh.toShape(tableMesh, color=(10/255, 108/255, 3/255)))

    lona = createPlane(tex_pipeline, "lona", "lona")
    lona.setRotation([90, 0, 0])
    lona.setPosition([0, 0, -0.26])
    lona.setScale([25.66, 1, 13.33])

    amortiguador = GameObject("amortiguador", pipeline)
    amortiguador.setModel(tableShape)
    amortiguador.setScale([12.33, 0.6, 0.56])

    a1 = GameObject("a1", pipeline)
    a1.addChilds([amortiguador])
    a1.setRotation([0, 0, 90])
    a1.setPosition([-12.8, 0, 0])

    a2 = GameObject("a2", pipeline)
    a2.addChilds([amortiguador])
    a2.setRotation([0, 0, -90])
    a2.setPosition([12.8, 0, 0])

    a3 = GameObject("a3", pipeline)
    a3.addChilds([amortiguador])
    a3.setPosition([6.35, 6.35, 0])

    a4 = GameObject("a4", pipeline)
    a4.addChilds([amortiguador])
    a4.setPosition([-6.35, 6.35, 0])

    a5 = GameObject("a5", pipeline)
    a5.addChilds([amortiguador])
    a5.setRotation([0, 0, 180])
    a5.setPosition([6.35, -6.35, 0])

    a6 = GameObject("a6", pipeline)
    a6.addChilds([amortiguador])
    a6.setRotation([0, 0, 180])
    a6.setPosition([-6.35, -6.35, 0])

    h1 = GameObject("h1", tex_pipeline)
    h1.addChilds([holeModel])
    h1.setPosition([0, -6.1, 0])

    h2 = GameObject("h2", tex_pipeline)
    h2.addChilds([holeModel])
    h2.setPosition([0, 6.1, 0])

    h3 = GameObject("h3", tex_pipeline)
    h3.addChilds([holeModel])
    h3.setPosition([12.5, 6.1, 0])

    h4 = GameObject("h4", tex_pipeline)
    h4.addChilds([holeModel])
    h4.setPosition([-12.5, 6.1, 0])

    h5 = GameObject("h5", tex_pipeline)
    h5.addChilds([holeModel])
    h5.setPosition([-12.5, -6.1, 0])

    h6 = GameObject("h6", tex_pipeline)
    h6.addChilds([holeModel])
    h6.setPosition([12.5, -6.1, 0])



    table = GameObject("table", pipeline)
    table.addChilds([a1, a2, a3, a4, a5, a6 ,h1, h2, h3, h4, h5, h6, lona])
    return table