import graphics

# Initialize graphics before importing other modules
graphics.init()


import game

print(f"Window opened at width {graphics.WIDTH} and height {graphics.HEIGHT}")
game.run()
graphics.quit()
print(game.game_board)
