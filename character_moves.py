from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def moveRectangle():
    print("move Rectangle")
    clear_canvas_now()
    character.draw_now(400, 90)
    grass.draw_now(400, 30)
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
