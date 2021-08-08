import pygame
import random

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
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
        # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        pygame.display.flip()
    pygame.quit()

