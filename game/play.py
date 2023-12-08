import graphics
import game

game_board = game.initialize_array()

def play_game():
    """
    Initializes and starts the game
    """
    graphics.initialize_grid()
    graphics.draw_on_board()
    graphics.update_screen()
    winner = game.verify_winner()
    is_grid_full = game.is_grid_full()
    if winner != None:
        if winner == 1: 
            print("Le joueur X à gagné")
        else:
            print("Le joueur O à gagné")
        game.stop_running()
    if is_grid_full:
        print("Egalité!")
        game.stop_running()