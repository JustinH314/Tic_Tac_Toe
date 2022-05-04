# import
from pathlib import Path
import pygame
import random
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
        self.status = create_2D()
    
    def is_valid_move(self, row, col):
        return self.status[row][col] == 0

    def move(self, row, col, player):
        self.status[row][col] = player

def init_player(players):
    # return random.randint(*players)
    return 2

def create_2D():
    # [[1, 2, 3],
    #  [4, 5, 6],
    #  [7, 8, 9]]
    x = []
    for i in range(3):
        row = []
        
        for j in range(3):
            row.append(0)
        
        x.append(row)
    return x    

if "__main__" == __name__:
    running = True

    # initialization
    pygame.init()
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Tic Tac Toe")

    background = pygame.image.load(Path(ASSETS_DIR) / BACKGROUND_IMAGE)
    board = Board()
    player = init_player([1, 2])
    sign_mapping = {
        1: CIRCLE_IMAGE,
        2: CROSS_IMAGE
    }
    group = pygame.sprite.Group()
    crosshair = Crosshair(CROSSHAIR_IMAGE)
    group.add(crosshair)
    # circle = Sign(CIRCLE_IMAGE, (100, 100))
    # cross = Sign(CROSS_IMAGE, (, x))
    # group.add(circle)
    # group.add(cross)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = event.pos
                print(f"pos_x {pos_x}, pos_y {pos_y}")
                if not (pos_x <= board.size and pos_y <= board.size):
                    continue
                (_, _, width, height) = board.surface.get_rect()
                col = int(pos_x // (width/3))
                row = int(pos_y // (height/3))
                print(f"row {row}, col {col}")

                if board.is_valid_move(row, col):
                    board.move(row, col, player)
                    sign = Sign(sign_mapping[player], (col*CELL_DELTA+CELL_ORIGIN, row*CELL_DELTA+CELL_ORIGIN))
                    group.add(sign)
                    group.add(crosshair)
                    print(board.status)

        screen.blit(background, (0, 0))
        screen.blit(board.surface, (0, 0))
        group.draw(screen)
        group.update()
        clock.tick(60)
        pygame.display.flip()
