
import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
import game
import graphics
import inputs

menu = None
player_symbol = 1

from typing import Tuple, Any
def set_symbol(selected: Tuple, value: Any) -> None:
    """
    Set the symbol of the player.
    """
    global player_symbol
    player_symbol = value
    inputs.set_turn(player_symbol)
    
def get_symbol():
    global player_symbol
    return player_symbol
    
def button_play_action():
    global menu
    game.change_current_state(game.PLAY_GAME)
    menu.disable()

    
def menu():
    global menu
    
    menu = pygame_menu.Menu(
    height=500,
    theme=pygame_menu.themes.THEME_DARK,
    title='TIC TAC TOE',
    width=500
    )
    screen = graphics.get_screen()
    user_name = menu.add.text_input('Name: ', default='Username', maxchar=10)
    menu.add.selector('Choisir ', [('X', 1), ('O', -1)], onchange=set_symbol)
# menu.add.selector('Difficulté: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add.button('Historique')
    menu.add.button('Jouer',button_play_action)
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(screen)
    

