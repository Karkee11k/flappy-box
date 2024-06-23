import pygame
from box import Box
from settings import Settings

pygame.init()
pygame.display.set_mode((800, 700))
image = Settings().images['pipes']
player = image[0]
width, height = player.get_width(), player.get_height()
print("width x height: ", width, height)
for x in range(width):
    for y in range(height):
        if player.get_at((x, y))[3] == 0:
            print(x, y, end=', ')