import pygame
import inputs
import game

RUNNING = True
MENU = 0
PLAY_GAME = 1
GAME_OVER = 2
current_state = MENU


def change_current_state(state):
    """
    Change the current state of the game: 0 for the menu - 1 for the game
    """
    global current_state
    current_state = state

 
def stop_running():
	"""
	Stops the main loop.
	"""
	global RUNNING
	RUNNING = False



def run():
    """
    The main loop of the game.
    """
    global RUNNING
    while RUNNING == True:
        if current_state == MENU:
            game.menu()
        elif current_state == PLAY_GAME:
            game.play_game()
        elif current_state == GAME_OVER:
            pass
        inputs.handle_inputs()
