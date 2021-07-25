import meshes as mh
from gameobject import GameObject
from BilliardBalls import Bball
from shadow import Shadow
from trayectoria import Trayectoria
from cue import Cue
from plane3d import Plane3D
from hudPlane import HudPlane
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
    ballShape = createNormalBall(20)
    ballModel = GameObject("bola"+ number + "model", tex_pipeline)
    ballModel.setRotation([0, 90, 0])
    path = "assets/" + "b" + number + ".png"
    ballModel.setModel(createTextureGPUShape(ballShape, tex_pipeline, path), True)

    ball = Bball("bola" + number, tex_pipeline, posXY, int(number))
    ball.addChilds([ballModel])

    return ball


def createBalls(tex_pipeline):
    shadowPath = "assets/shadow.png"
    arrowPath = "assets/arrow.png"

    balls = []
    shadows = []
    arrows = []

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
        shadow.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, shadowPath, False), True)
        shadow.setRotation([90, 0, 0])
        shadows.append(shadow)

        arrow = Trayectoria("flecha", tex_pipeline)
        arrow.ball = ball
        arrow.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, arrowPath, False), True)
        arrow.setRotation([90, 0, 0])
        arrows.append(arrow)



    ballSet.addChilds(shadows)
    ballSet.addChilds(arrows)

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

def createHud(tex_pipeline):
    barPath = "assets/bar1.png"

    bar = HudPlane("barra", tex_pipeline)
    bar.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, barPath, False), True)
    return bar

def createTable(pipeline, tex_pipeline):

    holePath = "assets/shadow.png"
    woodPath = "assets/wood.png"

    sideModel = GameObject("side", tex_pipeline)
    sideModel.setModel(createTextureGPUShape(bs.createTextureNormalsCube(), tex_pipeline, woodPath , True), True)

    holeModel = GameObject("hole", tex_pipeline)
    holeModel.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, holePath, False), True)
    holeModel.setRotation([90, 0, 0])
    holeModel.setPosition([0, 0, -0.259])

    amortiguadorMesh = mh.createAmortiguador()
    amortiguadorShape = createGPUShape(pipeline, mh.toShape(amortiguadorMesh, color=(10/255, 108/255, 3/255)))

    lona = createPlane(tex_pipeline, "lona", "lona")
    lona.setRotation([90, 0, 0])
    lona.setPosition([0, 0, -0.26])
    lona.setScale([27.75, 1, 13.33])

    amortiguador = GameObject("amortiguador", pipeline)
    amortiguador.setModel(amortiguadorShape)
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

    amortiguadores = GameObject("amortiguadores", pipeline)
    amortiguadores.addChilds([a1, a2, a3, a4, a5, a6])

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

    holes = GameObject("holes", tex_pipeline)
    holes.addChilds([h1, h2, h3, h4, h5, h6])

    s1 = GameObject("s1", tex_pipeline)
    s1.addChilds([sideModel])
    s1.setScale([27.75, 0.75, 0.56])
    s1.setPosition([0, 7, 0])

    s2 = GameObject("s2", tex_pipeline)
    s2.addChilds([sideModel])
    s2.setScale([27.75, 0.75, 0.56])
    s2.setPosition([0, -7, 0])

    s3 = GameObject("s3", tex_pipeline)
    s3.addChilds([sideModel])
    s3.setRotation([0, 0, 90])
    s3.setScale([13.25, 0.75, 0.56])
    s3.setPosition([13.5, 0, 0])

    s4 = GameObject("s4", tex_pipeline)
    s4.addChilds([sideModel])
    s4.setRotation([0, 0, 90])
    s4.setScale([13.25, 0.75, 0.56])
    s4.setPosition([-13.5, 0, 0])

    sides = GameObject("sides", tex_pipeline)
    sides.addChilds([s1, s2, s3, s4])

    l1 = GameObject("l1", tex_pipeline)
    l1.addChilds([sideModel])
    l1.setRotation([0, 90, 0])
    l1.setScale([5.25, 0.75, 0.56])
    l1.setPosition([-13.5, 7, -2.5])

    l2 = GameObject("l2", tex_pipeline)
    l2.addChilds([sideModel])
    l2.setRotation([0, 90, 0])
    l2.setScale([5.25, 0.75, 0.56])
    l2.setPosition([-13.5, -7, -2.5])

    l3 = GameObject("l3", tex_pipeline)
    l3.addChilds([sideModel])
    l3.setRotation([0, 90, 0])
    l3.setScale([5.25, 0.75, 0.56])
    l3.setPosition([13.5, 7, -2.5])

    l4 = GameObject("l4", tex_pipeline)
    l4.addChilds([sideModel])
    l4.setRotation([0, 90, 0])
    l4.setScale([5.25, 0.75, 0.56])
    l4.setPosition([13.5, -7, -2.5])

    legs = GameObject("legs", tex_pipeline)
    legs.addChilds([l1, l2, l3, l4])




    table = GameObject("table", pipeline)
    table.addChilds([amortiguadores, holes, sides, legs, lona])
    return table

def createScene(pipeline, tex_pipeline, controller):

    bolas = createBalls(tex_pipeline)
    cue = createCue(pipeline, controller)
    mesa = createTable(pipeline, tex_pipeline)

    for bola in bolas.childs:
        if not isinstance(bola, Bball):
            continue
        controller.ballList += [bola]

    scene = GameObject("scene", pipeline)
    scene.addChilds([bolas, cue, mesa])

    return scene