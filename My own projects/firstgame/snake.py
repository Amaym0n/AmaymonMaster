import pygame
import random
import time

WIDTH = 360
HEIGHT = 480
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


if __name__ == "__main__":
# создаем игру и окно
    pygame.init()
    pygame.mixer.init()  # для звука
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("David's snake")
    clock = pygame.time.Clock()
    print(clock)

    while True:
        screen.fill(WHITE)
        pygame.display.flip()
        time.sleep(5)
        break

