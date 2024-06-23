import pygame
import sys

from game_stats import GameStats
from transition import GameTransition

def checkEvents(stats: GameStats, transition: GameTransition) -> None:
    """Responds to events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            checkKeydowns(event, stats, transition)

def checkKeydowns(event, stats: GameStats, transition: GameTransition):
    """Responds to key press events."""
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
        if stats.gameState == GameStats.ACTIVE:
            transition.box.flapped = True
        elif stats.gameState == GameStats.GET_READY:
            stats.gameState = GameStats.ACTIVE
        elif stats.gameState == GameStats.END:
            transition.newGame()