from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def R_moveLeft():
    pass

def R_moveRight():
    pass

def R_moveUP():
    pass

def R_moveDown():
    pass


def moveRectangle():
    print("move Rectangle")

    R_moveLeft()
    R_moveUP()
    R_moveRight()
    R_moveDown()

    pass

def moveTriangle():
    print("move Triangle")
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
