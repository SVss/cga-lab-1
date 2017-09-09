import sys
from sdl2 import *
import sdl2.ext as sdl2ext
from math import pi, sin, cos, trunc

CENTER_X = 100
CENTER_Y = 100

COEFF_A = 100
STEP = 0.01

def draw(surface):
    sdl2ext.fill(surface, 0)
    color = sdl2ext.Color(255, 255, 255)
    points = []

    # points += [10, 10, 20, 20, 20, 20, 30, 30,]

    points.append(CENTER_X)
    points.append(CENTER_Y)

    t = 0
    while t <= 2*pi:
        x = trunc(COEFF_A * cos(t) * (1*cos(t))) + CENTER_X
        y = trunc(COEFF_A * sin(t) * (1*sin(t))) + CENTER_Y

        points.append(x)
        points.append(y)

        points.append(x)
        points.append(y)

        t += STEP;

    points.append(CENTER_X)
    points.append(CENTER_Y)

    sdl2ext.line(surface, color, points)


def main():
    sdl2ext.init()
    window = sdl2ext.Window("2D drawing primitives", size=(500, 500))
    window.show()

    surface = window.get_surface()
    
    running = True
    while running:
        events = sdl2ext.get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
                break
        draw(surface)
        window.refresh()
    sdl2ext.quit()

    return 0


if __name__ == "__main__":
    # COEFF_A = float(input("Enter 'a' value:"))
    # STEP = input("Enter 'a' value:")
    sys.exit(main())