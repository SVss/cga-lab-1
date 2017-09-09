import sys
from sdl2 import *
import sdl2.ext as sdl2ext
from math import pi, sin, cos, trunc

CENTER_X = 100
CENTER_Y = 100

COEFF_A = 100
STEP = 0.01


def draw(surface):
    sdl2ext.fill(surface, 0xFFFFFF)
    color = sdl2ext.Color(0, 0, 0)
    points = []
    t = 0
    while t < 2*pi:
        x = trunc(COEFF_A * cos(t) * (1 + cos(t))) + CENTER_X
        y = trunc(COEFF_A * sin(t) * (1 + cos(t))) + CENTER_Y
        points += [(x, y)]
        t += STEP
    
    SDL_LockSurface(surface)
    
    # TODO: Manipulate with pixels directly

    SDL_UnlockSurface(surface)


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