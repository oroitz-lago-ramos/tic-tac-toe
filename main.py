import pygame
from config import *
from events import *
from grid import *
from verification import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()  

isRunning = True
isClicked = False
mouse_position = []
game_board = initialize_array()
player_turn = 1

while isRunning:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.MOUSEBUTTONDOWN and isClicked == False:
            isClicked = True
            mouse_position = pygame.mouse.get_pos()
            cell_x = mouse_position[0]
            cell_y = mouse_position[1]
        elif event.type == pygame.MOUSEBUTTONUP and isClicked == True:
            isClicked = False
            mouse_position = pygame.mouse.get_pos()
            cell_x = mouse_position[0] // X_CELL  
            cell_y = mouse_position[1] // Y_CELL 

            if game_board[cell_y][cell_x] == 0:
                game_board[cell_y][cell_x] = player_turn
                player_turn *= -1

    winner = verify_winner(game_board)
    if winner != None:
        isRunning = False
        if winner == 1:
            print("Le joueur X gagne")
        elif winner == -1:
            print("Le joueur O gagne")
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    initialize_grid(screen)
    draw_on_board(screen,game_board)
    
    
    
    
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    isFull = is_grid_full(game_board)
    if isFull:
        isRunning = False
        print("Pas de gagnant!")
    
    
    clock.tick(60)  # limits FPS to 60
    isRunning = escape_button(isRunning)
pygame.quit()


