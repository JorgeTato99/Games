"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

"Se crea una ventana la cual simula un canvas, en la cual se debe de de dar click para lanzar una bola la cual revienta los globos"
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(100, 150)
targets = []

"Se define la funcion de Tap, el cual es el encargado de ver responder a los clicks del mouse"
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

"Se define la función draw el cual hace que se ponga el tamaño y color de los globos, como el de los cañones."
"En este caso se puso que el globo fuera azul y tamaño 20. El cañon sera de color rojo con un tamaño 5"
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

"Se define la función move, el cual aplica la gravedad, el efecto de gravedad y su velocidad del cañon"
"Aqui se modifica como es que estara trabajando la bola de cañon y como es que se movera dentro del juego"
def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.25
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
