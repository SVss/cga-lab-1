import sys
from math import pi, sin, cos, trunc
import ctypes
import sdl2
import sdl2.ext

STEP = 0.01
A_COEFF = 100
CENTER_X = 100
CENTER_Y = 200


def draw(renderer):
    sdl2.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0)
    sdl2.SDL_RenderClear(renderer)
    sdl2.SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255)

    points_set = set()

    a = A_COEFF
    t = 0
    while t < 2 * pi:
        p = a * cos(t) * (1 + cos(t)) + CENTER_X
        y = a * sin(t) * (1 + cos(t)) + CENTER_Y
        points_set.add((trunc(p), trunc(y)))
        t += STEP

    points_count = len(points_set)
    points_array = (sdl2.SDL_Point*points_count)(*[sdl2.SDL_Point(p[0], p[1]) for p in points_set])

    sdl2.SDL_RenderDrawPoints(renderer, points_array, points_count)
    sdl2.SDL_RenderPresent(renderer)


def main():
    sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
    window = sdl2.SDL_CreateWindow(b"Lab 1 - Cardioid",
                                   sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
                                   500, 500, sdl2.SDL_WINDOW_SHOWN, sdl2.SDL_WINDOW_RESIZABLE)
    # CREATE !!!
    renderer = sdl2.SDL_CreateRenderer(
        window, -1, sdl2.SDL_RENDERER_ACCELERATED)

    running = True
    event = sdl2.SDL_Event()
    while running:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        draw(renderer)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
