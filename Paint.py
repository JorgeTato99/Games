"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
"""Se crea una ventana la cual simula un canvas, donde se puede dibujar
   lineas, cuadrados, rectangulos, triangulos y circulos de diferentes
   colores.
"""

from turtle import *
from freegames import vector

"""Se define la funcion line, la cual recibe dos coordenadas
   como parametro. La funcion dibuja una linea apartir de la
   primera coordenada hasta la segunda.
"""
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

"""Se define la funcion square, la cual recibe dos coordenada,
   las cuales va a equivaler el tamaño de los lados del cuadrado.
   Dentro de un ciclo for se dibuja el lado y se cambia la direccion
   del cursor 90 grados, esto se ejecuta cuatro veces.
"""    
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

"""Se define la funcion circulo, la cual recibe dos coordenada
   para formar la figura de un circulo, siendo la distancia de
   estos dos puntos el tamaño de la circunferencia del circulo.
"""
def circle(start, end):
    "Draw circle from start to end."
    seccion = (end.x - start.x)/13 #Calcula el tamaño de las secciones
    up()
    goto(start.x, start.y)

    #Se posiciona el cursor en la segunda coordenada
    forward(end.x - start.x)
    left(95) #Se ubica el diametro a la mitad del circulo
    down()
    begin_fill()

    #Se dibujan las secciones 40 veces
    for count in range(40):
        forward(seccion)
        left(9)

    left(265) #Se regresa el cursor a su direccion original
    end_fill()

 """Se define la funcion rectangle, la cual recibe dos coordenadas,
    con las cuales se define la el tamaño de la base y la altura de
    un rectangulo. Desntro de un for se dibuja primero la base, se
    cambia la direccion del cursor 90 grados y se dibuja la altura
    para despues volver a cambiar de direccion 90 grados, esto se 
    repite dos veces.
 """   
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x) #Se dibuja la base
        left(90)
        forward(end.y - start.y) #Se dibuja la altura
        left(90)

    end_fill()

"""Se define la funcion triangle, la cual recibe dos coordenadas
   como parametro, las cuales definen el tamaño de los lados del
   triangulo. Dentro de un ciclo for, se dibuja un lado del 
   triangulo y se cambia la direccion 120 grados.
"""
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill
    
    for count in range(3):
        forward(end.x - start.x)
        left(120)
       
    end_fill()

"""Se define la funcion tap, la cual recibe los valores de x e y
   de una coordenada. Cuando no hay ningun valor como la
   coordenada inicial, se le asigna estos valores, si la
   coordenada inicial ya tiene valores, se le asiganan los valores
   dados como parametro a la coordenada final.
"""
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

"""Se define la funcion store, la cual asigan la funcion de alguna
   figura shape.
"""
def store(key, value):
    "Store value in state at key."
    state[key] = value

"""Se inicializan los valores y se definen teclas a pulsar para elegir
   los coleres y las figuras.
"""
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
