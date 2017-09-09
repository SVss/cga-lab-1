import sys
import ctypes
from sdl2 import *


def draw(renderer):
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
    SDL_RenderClear(renderer);     
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);

    points = []
    points.append(SDL_Point(10, 10))

    arr = (SDL_Point * len(points))(*points)

    SDL_RenderDrawLine(renderer, 10, 10, 20, 20)
    SDL_RenderPresent(renderer);


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Lab 1 - Cardioid",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              500, 500, SDL_WINDOW_SHOWN, SDL_WINDOW_RESIZABLE)
    renderer = SDL_GetRenderer(window)

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