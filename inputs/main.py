import pygame
import game
import inputs
import graphics

isClicked = False
turn = 1

def set_turn(t):
    global turn
    turn = t

def handle_inputs():
	"""
	Handles all the inputs.
	"""
	global isClicked
	global turn
	keys = pygame.key.get_pressed()
	if (pygame.event.peek(pygame.QUIT)):
		game.stop_running()
	if (keys[pygame.K_ESCAPE]):
		game.stop_running()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN and isClicked == False:
			isClicked = True
			mouse_position = pygame.mouse.get_pos()
			cell_x = mouse_position[0]
			cell_y = mouse_position[1]
		elif event.type == pygame.MOUSEBUTTONUP and isClicked == True:
			isClicked = False
			mouse_position = pygame.mouse.get_pos()
			cell_x = mouse_position[0] // graphics.CELL_SIZE
			cell_y = mouse_position[1] // graphics.CELL_SIZE

			if game.game_board[cell_y][cell_x] == 0:
				game.game_board[cell_y][cell_x] = turn
				turn *= -1
                # placement de ia
                # turn *= -1 on revient sur mon tour