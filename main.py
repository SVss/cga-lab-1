import sys
from math import pi, sin, cos, trunc
import ctypes
import sdl2
import sdl2.ext

STEP = 0.001
A_COEFF_RELATION = 1 / 5

DEFAULT_WINDOW_WIDTH = 500
DEFAULT_WINDOW_HEIGHT = 500

C_BLACK = (0, 0, 0, 0)
C_RED = (255, 0, 0, 0)
C_BLUE = (0, 255, 0, 0)

PARTS = [
    (0, 2 * pi, C_BLACK)
]


def draw(renderer, window_size):
    sdl2.SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255)
    sdl2.SDL_RenderClear(renderer)

    a_base = min(window_size)
    a = A_COEFF_RELATION * a_base
    for part in PARTS:
        points_set = set()
        c_r, c_g, c_b, c_a = part[2]
        sdl2.SDL_SetRenderDrawColor(renderer, c_r, c_g, c_b, c_a)
        t = part[0]
        while t < part[1]:
            x = a * cos(t) * (1 + cos(t)) + window_size[0] / 2 - a
            y = a * sin(t) * (1 + cos(t)) + window_size[1] / 2
            points_set.add((trunc(x), trunc(y)))
            t += STEP

        points_count = len(points_set)
        points_list = [sdl2.SDL_Point(p[0], p[1]) for p in points_set]
        points_array = (sdl2.SDL_Point * points_count)(*points_list)

        sdl2.SDL_RenderDrawPoints(renderer, points_array, points_count)

    sdl2.SDL_RenderPresent(renderer)


def main():
    window_size = (DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)
    sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
    window = sdl2.SDL_CreateWindow(b"Lab 1 - Cardioid",
                                   sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
                                   window_size[0], window_size[1], sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_RESIZABLE)
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
            elif event.type == sdl2.SDL_WINDOWEVENT:
                if event.window.event == sdl2.SDL_WINDOWEVENT_SIZE_CHANGED:
                    new_width = event.window.data1
                    new_height = event.window.data2
                    print("Window {} resized to {}x{}".format(event.window.windowID,
                                                              new_width, new_height))
                    window_size = (new_width, new_height)
            draw(renderer, window_size)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
