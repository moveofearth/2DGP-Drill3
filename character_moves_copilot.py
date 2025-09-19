from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def draw_scene(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(int(x), int(y))
    delay(0.01)

def move_line(x1, y1, x2, y2, step=2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)
    steps = int(distance / step)
    for i in range(steps + 1):
        t = i / steps
        x = x1 + dx * t
        y = y1 + dy * t
        draw_scene(x, y)

def move_rectangle():
    # 사각형 경로: (400,90)→(780,90)→(780,570)→(10,570)→(10,90)→(400,90)
    move_line(400, 90, 780, 90)
    move_line(780, 90, 780, 570)
    move_line(780, 570, 10, 570)
    move_line(10, 570, 10, 90)
    move_line(10, 90, 400, 90)

def move_triangle():
    # 삼각형 경로: (400,90)→(780,90)→(400,570)→(10,90)→(400,90)
    move_line(400, 90, 780, 90)
    move_line(780, 90, 400, 570)
    move_line(400, 570, 10, 90)
    move_line(10, 90, 400, 90)

def move_circle():
    # 원 경로: 중심(400,316), 반지름 225, 0~360도
    cx, cy, r = 400, 316, 225
    for deg in range(0, 360):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        draw_scene(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()

