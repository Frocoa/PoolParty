import meshes as mh
from gameobject import GameObject
from BilliardBalls import Bball
from bar import Bar
from message import Message
from shadow import Shadow
from trayectoria import Trayectoria
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

def createBilliardBall(tex_pipeline, number, posXY, controller):
    number = str(number)
    ballShape = createNormalBall(20)
    ballModel = GameObject("bola"+ number + "model", tex_pipeline)
    ballModel.setRotation([0, 90, 0])
    path = "assets/" + "b" + number + ".png"
    ballModel.setModel(createTextureGPUShape(ballShape, tex_pipeline, path), True)

    ball = Bball("bola" + number, tex_pipeline, posXY, int(number), controller)
    ball.addChilds([ballModel])

    return ball


def createBalls(tex_pipeline, controller):
    shadowPath = "assets/shadow.png"
    arrowPath = "assets/arrow.png"

    balls = []
    shadows = []
    arrows = []

    b1 = createBilliardBall(tex_pipeline, 1, [0, 0], controller)
    b1.setScale([0.52, 0.52, 0.52])
    b1.setRotation([0, 25, 0])
    balls.append(b1)

    b2 = createBilliardBall(tex_pipeline, 2, [-0.52, -0.26], controller)
    b2.setScale([0.52, 0.52, 0.52])
    balls.append(b2)

    b3 = createBilliardBall(tex_pipeline, 3, [-1.04, -0.52], controller)
    b3.setScale([0.52, 0.52, 0.52])
    balls.append(b3)

    b4 = createBilliardBall(tex_pipeline, 4, [-1.56, -0.78], controller)
    b4.setScale([0.52, 0.52, 0.52])
    balls.append(b4)

    b5 = createBilliardBall(tex_pipeline, 5, [-2.08, 1.04], controller)
    b5.setScale([0.52, 0.52, 0.52])
    balls.append(b5)

    b6 = createBilliardBall(tex_pipeline, 6, [-2.08, -0.52], controller)
    b6.setScale([0.52, 0.52, 0.52])
    balls.append(b6)

    b7 = createBilliardBall(tex_pipeline, 7, [-1.56, 0.26], controller)
    b7.setScale([0.52, 0.52, 0.52])
    balls.append(b7)

    b8 = createBilliardBall(tex_pipeline, 8, [-1.04, 0], controller)
    b8.setScale([0.52, 0.52, 0.52])
    balls.append(b8)

    b9 = createBilliardBall(tex_pipeline, 9, [-0.52, 0.26], controller)
    b9.setScale([0.52, 0.52, 0.52])
    balls.append(b9)

    b10 = createBilliardBall(tex_pipeline, 10, [-1.04, 0.52], controller)
    b10.setScale([0.52, 0.52, 0.52])
    balls.append(b10)

    b11 = createBilliardBall(tex_pipeline, 11, [-1.56, 0.78], controller)
    b11.setScale([0.52, 0.52, 0.52])
    balls.append(b11)

    b12 = createBilliardBall(tex_pipeline, 12, [-2.08, -1.04], controller)
    b12.setScale([0.52, 0.52, 0.52])
    balls.append(b12)

    b13 = createBilliardBall(tex_pipeline, 13, [-2.08, 0.52], controller)
    b13.setScale([0.52, 0.52, 0.52])
    balls.append(b13)

    b14 = createBilliardBall(tex_pipeline, 14, [-1.56, -0.26], controller)
    b14.setScale([0.52, 0.52, 0.52])
    balls.append(b14)

    b15 = createBilliardBall(tex_pipeline, 15, [-2.08, 0], controller)
    b15.setScale([0.52, 0.52, 0.52])
    balls.append(b15)

    bcue = createBilliardBall(tex_pipeline, 0, [4, 0], controller)
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
    cueModel.setRotation([98, 0, 0])
    cueModel.setScale([0.6, 0.6, 10])
    cueModel.setPosition([0, 1, 0])

    cueCenter = Cue("cue", pipeline, controller)
    cueCenter.addChilds([cueModel])
    cueCenter.setPosition([4, 0, 0])
    cueCenter.setRotation([0, 0, -90])
    
    return cueCenter

def createBar(bar_tex, tex_pipeline, controller):
    barPath = "assets/bar1.png"
    barPath2 = "assets/bar2.png"
    letrasPath = "assets/unidadfuerza.png"

    outline = GameObject("borde", tex_pipeline)
    outline.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, barPath2, False), True)

    charge = Bar("carga", bar_tex, controller, outline)
    charge.setModel(createTextureGPUShape(createTextureNormalPlane(), bar_tex, barPath, False), True)

    leyenda = GameObject("leyenda", tex_pipeline)
    leyenda.setModel(createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, letrasPath, False), True)
    leyenda.setRotation([0, 0, 180])
    leyenda.setPosition([0.13, 0, 0])
    
    bar = GameObject("barra", tex_pipeline)
    bar.addChilds([outline, charge, leyenda])
    bar.setScale([3.8, 1, 3.8])
    bar.setRotation([90, 180, 0])
    bar.setPosition([13, -7.1, 19])



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

def createMessage(tex_pipeline, controller):
    pathRK4 = "assets/rk4.png"
    pathEuler = "assets/euler.png"
    pathEulerMejorado = "assets/eulermejorado.png"
    pathEulerModificado = "assets/eulermodificado.png"

    rk4 = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, pathRK4)
    euler = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, pathEuler)
    euler_mejorado = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, pathEulerMejorado)
    euler_modificado = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, pathEulerModificado)

    message = Message("mensaje", tex_pipeline, controller)
    message.setModel(rk4, True)
    message.addModels([rk4, euler, euler_mejorado, euler_modificado])
    message.setScale([10, 10, 10])

    return message

def createAmbient(tex_pipeline, pipeline):
    path1 = "assets/fondo1.png"
    path2 = "assets/fondo2.png"
    path3 = "assets/fondo3.png"
    path4 = "assets/fondo4.png"
    path5 = "assets/fondo5.png"
    path6 = "assets/fondo6.png"

    fondo1 = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, path1)
    fondo2 = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, path2)
    fondo3 = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, path3)
    fondo4 = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, path4)
    fondo5 = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, path5)
    fondo6 = createTextureGPUShape(createTextureNormalPlane(), tex_pipeline, path6)

    muro1 = GameObject("muro1", tex_pipeline)
    muro1.setModel(fondo1)
    muro1.setScale([100, 20, 70])
    muro1.setPosition([0, 50, 0])

    muro2 = GameObject("muro2", tex_pipeline)
    muro2.setModel(fondo2)
    muro2.setRotation([0, 0, -90])
    muro2.setScale([100, 20, 70])
    muro2.setPosition([50, 0, 0])

    muro3 = GameObject("muro3", tex_pipeline)
    muro3.setModel(fondo3)
    muro3.setScale([100, 20, 70])
    muro3.setRotation([0, 0, 180])
    muro3.setPosition([0, -50, 0])

    muro4 = GameObject("muro4", tex_pipeline)
    muro4.setModel(fondo4)
    muro4.setScale([100, 20, 70])
    muro4.setRotation([0, 0, 90])
    muro4.setPosition([-50, 0, 0])

    techo = GameObject("techo", tex_pipeline)
    techo.setModel(fondo5)
    techo.setScale([120, 120, 120])
    techo.setRotation([90, 0, 0])
    techo.setPosition([0, 0, 25])

    suelo = GameObject("suelo", tex_pipeline)
    suelo.setModel(fondo6)
    suelo.setScale([120, 1, 120])
    suelo.setRotation([90, 0, 0])
    suelo.setPosition([0, 0, -10])

    murallas = GameObject("murallas", tex_pipeline)
    murallas.addChilds([muro1, muro2, muro3, muro4, techo, suelo])
    murallas.setPosition([0, 0, 5])

    return murallas

def createScene(pipeline, tex_pipeline, bar_tex, controller):

    bolas = createBalls(tex_pipeline, controller)
    cue = createCue(pipeline, controller)
    mesa = createTable(pipeline, tex_pipeline)
    mensaje = createMessage(tex_pipeline, controller)
    barra = createBar(bar_tex, tex_pipeline, controller)
    fondo = createAmbient(tex_pipeline, pipeline)

    for bola in bolas.childs:
        if not isinstance(bola, Bball):
            continue
        controller.ballList += [bola]

    scene = GameObject("scene", pipeline)
    scene.addChilds([bolas, cue, mesa, mensaje, barra, fondo])

    return scene