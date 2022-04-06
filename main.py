import pygame
import sys

BG_COLOR = (36, 106, 115)
HEIGHT = 600
WIDTH = 600
SCREEN_SIZE = (HEIGHT, WIDTH)
GAME_TITLE = "Tic Tac Toe"
STROKE_WIDTH = 5
STROKE_COLOR = (255, 255, 255)
SIGN_COLOR = (246, 174, 45)
CROSS_MARGIN = 40
def draw_line():
    pygame.draw.line(screen, STROKE_COLOR, (0, HEIGHT/3), (WIDTH, HEIGHT/3), STROKE_WIDTH)
    pygame.draw.line(screen, STROKE_COLOR, (0, HEIGHT/3*2), (WIDTH, HEIGHT/3*2), STROKE_WIDTH)
    pygame.draw.line(screen, STROKE_COLOR, (WIDTH/3, 0), (WIDTH/3, HEIGHT), STROKE_WIDTH)
    pygame.draw.line(screen, STROKE_COLOR, (WIDTH/3*2, 0), (WIDTH/3*2, HEIGHT), STROKE_WIDTH)

def draw_circle(row, col):
    pygame.draw.circle(screen, SIGN_COLOR, (int(col * WIDTH/3 + WIDTH/6), int(row * HEIGHT/3 + HEIGHT/6)), HEIGHT/6 * 0.7, STROKE_WIDTH)

    # [[1, 2, 3],
    #  [4, 5, 6],
    #  [7, 8, 9]]

def draw_cross(row, col):
    pygame.draw.line(screen,
                     SIGN_COLOR,
                     (int(col * WIDTH/3 + CROSS_MARGIN), int(row * HEIGHT/3 + CROSS_MARGIN)),
                     (int(col * WIDTH/3 + WIDTH/3 - CROSS_MARGIN), int(row * HEIGHT/3 + HEIGHT/3 - CROSS_MARGIN)), 
                     STROKE_WIDTH)
    pygame.draw.line(screen,
                     SIGN_COLOR,
                     (int(col * WIDTH/3 + CROSS_MARGIN), int(row * HEIGHT/3 + HEIGHT/3 - CROSS_MARGIN)),
                     (int(col * WIDTH/3 + WIDTH/3 - CROSS_MARGIN), int(row * HEIGHT/3 + CROSS_MARGIN)), 
                     STROKE_WIDTH)
#:%s/pattern/replace/g 

def draw_sign(player, row, col):
    if player == 0:
        draw_circle(row, col)
    elif player == 1:
        draw_cross(row, col)

if "__main__" == __name__:
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(GAME_TITLE)
    screen.fill(BG_COLOR)
    draw_line()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = event.pos
                col = int(pos_x // (WIDTH/3))
                row = int(pos_y // (HEIGHT/3))
                print(row, col)
                draw_cross(row, col)
        pygame.display.update()            
