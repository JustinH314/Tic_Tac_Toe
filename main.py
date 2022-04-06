import pygame
import sys

BG_COLOR = (36, 106, 115)
HEIGHT = 600
WIDTH = 600
SCREEN_SIZE = (HEIGHT, WIDTH)
GAME_TITLE = "Tic Tac Toe"
STROKE_WIDTH = 5
STROKE_COLOR = (255, 255, 255)
def draw_line():
    pygame.draw.line(screen, STROKE_COLOR, (0, HEIGHT/3), (WIDTH, HEIGHT/3), STROKE_WIDTH)
    pygame.draw.line(screen, STROKE_COLOR, (0, HEIGHT/3*2), (WIDTH, HEIGHT/3*2), STROKE_WIDTH)
    pygame.draw.line(screen, STROKE_COLOR, (WIDTH/3, 0), (WIDTH/3, HEIGHT), STROKE_WIDTH)
    pygame.draw.line(screen, STROKE_COLOR, (WIDTH/3*2, 0), (WIDTH/3*2, HEIGHT), STROKE_WIDTH)

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
                print(pos_x, pos_y)
        
        pygame.display.update()            
