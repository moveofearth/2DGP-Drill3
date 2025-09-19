from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')



def draw_scene(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)



def moveLeft():
    for i in range(780, 10, -2):
        draw_scene(i, 570)
    pass

def moveRight_1():
    for i in range (10, 400, 2):
        draw_scene(i, 90)
    pass

def moveRight_2():
    for i in range (400, 780, 2):
        draw_scene(i, 90)
    pass

def moveUP():
    for i in range (90, 570, 2):
        draw_scene(780, i)
    pass

def moveDown():
    for i in range (570, 90, -2):
        draw_scene(10, i)
    pass

def moveLUP():
    pass

def moveRDOWN():
    pass


def moveRectangle():
    print("move Rectangle")

    moveRight_2()
    moveUP()
    moveLeft()
    moveDown()
    moveRight_1()

    pass

def moveTriangle():
    print("move Triangle")

    moveRight_2()
    moveLUP()
    moveRDOWN()

    pass

def moveCircle():
    print("move Circle")
    pass

while True:
    moveRectangle()
    moveTriangle()
    moveCircle()
    pass

close_canvas()
