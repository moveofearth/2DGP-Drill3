from pico2d import *
import math

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
    startX = 780
    startY = 90
    endX = 400
    endY = 570

    dx = endX - startX
    dy = endY - startY

    step_count = int(dy / 5) + 1
    step_size_y = dy / step_count
    step_size_x = dx / step_count

    currentX = startX
    currentY = startY

    for i in range(step_count + 1):
        currentX = startX + (step_size_x * i)
        currentY = startY + (step_size_y * i)
        draw_scene(int(currentX), int(currentY))
    pass

def moveLDOWN():
    startX = 400
    startY = 570
    endX = 10
    endY = 90

    dx = endX - startX
    dy = endY - startY

    step_count = int(abs(dy) / 5) + 1
    step_size_y = dy / step_count
    step_size_x = dx / step_count

    currentX = startX
    currentY = startY

    for i in range(step_count + 1):
        currentX = startX + (step_size_x * i)
        currentY = startY + (step_size_y * i)
        draw_scene(int(currentX), int(currentY))
    pass


def moveRectangle():
    #print("move Rectangle")

    moveRight_2()
    moveUP()
    moveLeft()
    moveDown()
    moveRight_1()

    pass

def moveTriangle():
    #print("move Triangle")

    moveRight_2()
    moveLUP()
    moveLDOWN()
    moveRight_1()

    pass

def moveCircle():
    #print("move Circle")

    for i in range(270, 360):
        radian = math.radians(i)
        cx = 400 + 225 * math.cos(radian)
        cy = 316 + 225 * math.sin(radian)
        draw_scene(cx, cy)

    for i in range(0, 270):
        radian = math.radians(i)
        cx = 400 + 225 * math.cos(radian)
        cy = 316 + 225 * math.sin(radian)
        draw_scene(cx, cy)

    pass

while True:
    moveRectangle()
    moveTriangle()
    moveCircle()
    pass

close_canvas()
