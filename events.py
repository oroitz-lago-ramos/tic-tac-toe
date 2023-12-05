import pygame

def escape_button(isRunning):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        isRunning = False
    return isRunning