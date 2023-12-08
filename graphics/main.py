import pygame

WIDTH = 500
HEIGHT = 500
CELL_SIZE = WIDTH // 3
LINE_WIDTH = 3
MARKER_WIDTH = 2

_screen = None

def init():
	"""
	Initializes pygame and sets up the window.
	and any other graphics related stuff.
	"""
	global _screen
	pygame.init()
	pygame.display.set_caption("TIC TAC TOE")
	_screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
def get_screen():
    """
    Get the screen value -> Surface
    """
    return _screen

def update_screen():
    """
    Updates the screen
    """
    pygame.display.flip()
    
def quit():
	"""
	Shuts down pygame.
	"""
	pygame.quit()
