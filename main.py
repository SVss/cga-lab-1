import sys
import ctypes
from sdl2 import *
from math import pi, sin, cos, trunc

STEP = 0.01
A_COEFF = 100
CENTER_X = 100
CENTER_Y = 100

def draw(renderer):
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
    SDL_RenderClear(renderer);     
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);

    points = []

    a = A_COEFF
    t = 0
    while t < 2*pi:
        x = a*cos(t)*(1+cos(t)) + CENTER_X
        y = a*sin(t)*(1+cos(t)) + CENTER_Y
        points.append(SDL_Point(trunc(x), trunc(y)))
        t += STEP

    arr = (SDL_Point * len(points))(*points)

    SDL_RenderDrawPoints(renderer, arr, len(points))
    SDL_RenderPresent(renderer);


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Lab 1 - Cardioid",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              500, 500, SDL_WINDOW_SHOWN, SDL_WINDOW_RESIZABLE)
    # CREATE !!!
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)

    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
        draw(renderer)
    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())