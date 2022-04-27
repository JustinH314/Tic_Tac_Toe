# import
from pathlib import Path
from re import X
from tkinter import Y
import pygame
import sys


# game settings
ASSETS_DIR = "assets"
BACKGROUND_IMAGE = "background.jpg"
BOARD_IMAGE = "board.png"
CIRCLE_IMAGE = "circle.png"
CROSS_IMAGE = "cross.png"
CROSSHAIR_IMAGE = "crosshair 2.png"
CELL_DELTA = 195
CELL_ORIGIN = 30
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

class Sign(pygame.sprite.Sprite):
    def __init__(self, filename, coordinate, size = 1, length = 150):
        super().__init__()
        self.image = pygame.image.load(Path(ASSETS_DIR) / filename)
        self.image = pygame.transform.scale(self.image, (length, length))
        self.rect = pygame.Rect(coordinate[0], coordinate[1], size, size)

class Board:
    def __init__(self, size = 600):
        self.size = size
        self.surface = pygame.image.load(Path(ASSETS_DIR) / BOARD_IMAGE)
        self.surface = pygame.transform.scale(self.surface, (size, size))

if "__main__" == __name__:
    running = True

    # initialization
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Tic Tac Toe")

    background = pygame.image.load(Path(ASSETS_DIR) / BACKGROUND_IMAGE)
    board = Board()
    group = pygame.sprite.Group()
    crosshair = Crosshair(CROSSHAIR_IMAGE)
    # circle = Sign(CIRCLE_IMAGE, (100, 100))
    # cross = Sign(CROSS_IMAGE, (, x))
    # group.add(circle)
    # group.add(cross)
    group.add(crosshair)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = event.pos
                (_, _, width, height) = board.surface.get_rect()
                col = int(pos_x // (width/3))
                row = int(pos_y // (height/3))
                print(width, height)
        pygame.display.flip()
        screen.blit(background, (0, 0))
        screen.blit(board.surface, (0, 0))
        group.draw(screen)
        group.update()
