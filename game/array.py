def initialize_array():
    """
    Initializes the array 3 x 3 with 0 -> Array[[0,0,0][0,0,0][0,0,0]]
    """
    game_board = []
    for i in range(3):
        row = [0] * 3
        game_board.append(row)
    return game_board