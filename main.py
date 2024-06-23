import pygame

from game_stats import GameStats
from settings import Settings
import game_functions as gf
from transition import GameTransition


def run() -> None:
    """Runs the game's main loop."""
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy box')
    pygame.mouse.set_visible(False)
    settings = Settings()
    screen = pygame.display.set_mode(settings.screensize)
    stats = GameStats()
    transition = GameTransition(screen, settings, stats)
    
    while True:
        gf.checkEvents(stats, transition)
        if stats.gameState == GameStats.GET_READY: 
            transition.gameStart()
        elif stats.gameState == GameStats.ACTIVE: 
            transition.runGame()
        else:
            transition.gameOver()
        clock.tick(30)

run()