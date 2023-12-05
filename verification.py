def is_grid_full(game_board):
    for row in game_board:
        for cell in row:
            if cell == 0:  # If any cell is empty, return False
                return False
    return True

def verify_winner(game_board):
    # verify rows
    for x in game_board:
        if len(set(x)) == 1 and x[0] != 0:
            winner = x[0]
            return winner
        
    #  verify columns
    for col in range(len(game_board)):
        column_sum = 0
        for row in range(len(game_board)):
            column_sum += game_board[row][col]

        if column_sum == 3:
            return 1  
        elif column_sum == -3:
            return -1  

    # verify diags
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == 1 or game_board[0][2] == game_board[1][1] == game_board[2][0] == 1:
        return 1
    elif game_board[0][0] == game_board[1][1] == game_board[2][2] == -1 or game_board[0][2] == game_board[1][1] == game_board[2][0] == -1:
        return -1
    
                
    return None
