import pygame
from config import *

def initialize_grid(screen):
    for i in range(1,3):
        # Lignes horizontales
        pygame.draw.line(screen,'white',(0, i * Y_CELL),(SCREEN_HEIGHT, i * Y_CELL),LINE_WIDTH)
        # Lignes verticales
        pygame.draw.line(screen,'white',(i * X_CELL, 0),(i * X_CELL, SCREEN_WIDTH),LINE_WIDTH)
    
def initialize_array():
    game_board = []
    for i in range(3):
        row = [0] * 3
        game_board.append(row)
    return game_board
    
def draw_on_board(screen, game_board):
    x_pos = 0
    for x in game_board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, 'white',(y_pos * X_CELL + DIAG_1 , x_pos * Y_CELL + DIAG_1),(y_pos * X_CELL + DIAG_2, x_pos * Y_CELL + DIAG_2), MARKER_WIDTH)
                pygame.draw.line(screen, 'white',(y_pos * X_CELL + DIAG_1, x_pos * Y_CELL + DIAG_2),(y_pos * X_CELL + DIAG_2, x_pos * Y_CELL + DIAG_1), MARKER_WIDTH)
                
            if y == -1:
                pygame.draw.circle(screen, 'white', (y_pos * X_CELL + (X_CELL // 2), x_pos * Y_CELL + (Y_CELL // 2)), Y_CELL // 2 - 20, MARKER_WIDTH)
            y_pos += 1
        x_pos += 1
    
    
    