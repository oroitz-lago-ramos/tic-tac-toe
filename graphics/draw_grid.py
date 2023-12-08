import pygame
import graphics
from graphics import CELL_SIZE, WIDTH, HEIGHT, LINE_WIDTH, MARKER_WIDTH
import game

def initialize_grid():
    """
    Draws the empty game grid
    """
    screen = graphics.get_screen()
    screen.fill("black")
    for i in range(1,3):
        # Lignes horizontales
        pygame.draw.line(screen,'white',(0, i * CELL_SIZE),(WIDTH, i * CELL_SIZE),LINE_WIDTH)
        # Lignes verticales
        pygame.draw.line(screen,'white',(i * CELL_SIZE, 0),(i * CELL_SIZE, WIDTH),LINE_WIDTH)
    pygame.draw.line(screen, 'white', (0, 3 * CELL_SIZE + 1), (WIDTH, 3 * CELL_SIZE + 1), LINE_WIDTH)
    pygame.draw.line(screen, 'white', (0, 3 * CELL_SIZE + 1), (WIDTH, 3 * CELL_SIZE + 1), LINE_WIDTH)

def draw_on_board():
    """
    Displays the elements != 0 of the game_board element -> X ou O
    """
    screen = graphics.get_screen()
    x_pos = 0
    for x in game.game_board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, 'white',(y_pos * CELL_SIZE + 26 , x_pos * CELL_SIZE + 26),(y_pos * CELL_SIZE + 140, x_pos * CELL_SIZE + 140), MARKER_WIDTH)
                pygame.draw.line(screen, 'white',(y_pos * CELL_SIZE + 26, x_pos * CELL_SIZE + 140),(y_pos * CELL_SIZE + 140, x_pos * CELL_SIZE + 26), MARKER_WIDTH)
                
            if y == -1:
                pygame.draw.circle(screen, 'white', (y_pos * CELL_SIZE + (CELL_SIZE // 2), x_pos * CELL_SIZE +  CELL_SIZE // 2), CELL_SIZE // 2 - 20, MARKER_WIDTH)
            y_pos += 1
        x_pos += 1
    
    