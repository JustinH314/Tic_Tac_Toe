# import
from pathlib import Path
import pygame
import sys


# game settings
ASSETS_DIR = "assets"
BACKGROUND_IMAGE = "background.jpg"
CROSSHAIR_IMAGE = "crosshair 2.png"
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(Path(ASSETS_DIR) / filename)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


if "__main__" == __name__:
    running = True

    # initialization
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Tic Tac Toe")

    background = pygame.image.load(Path(ASSETS_DIR) / BACKGROUND_IMAGE)
    group = pygame.sprite.Group()
    crosshair = Crosshair(CROSSHAIR_IMAGE)
    group.add(crosshair)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()
        screen.blit(background, (0, 0))
        group.draw(screen)
        group.update()
