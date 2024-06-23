from pygame import SurfaceType

from game_stats import GameStats
from settings import Settings


class Scoreboard:
    """A class to represent the score """
    def __init__(self, screen: SurfaceType, settings: Settings, stats: GameStats):
        """Initializes the score board."""
        self.screen = screen
        self.screenWidth = settings.screensize[0]
        self.numbers = settings.numbers()
        self.messages = settings.messages()
        self.stats = stats
    
    def drawGetReady(self) -> None:
        """Draws 'Get Ready' on the screen."""
        x = (self.screenWidth - self.messages[0].get_width()) // 2
        self.screen.blit(self.messages[0], (x, 100)) 

    
    def drawGameOver(self) -> None:
        """Draws 'Game Over' on the screen."""
        x = (self.screenWidth - self.messages[1].get_width()) // 2
        self.screen.blit(self.messages[1], (x, 200)) 


    def drawScore(self) -> None:
        """Draws score on the screen."""
        score = [int(i) for i in str(self.stats.score)]
        totalWidth = 0
        for digit in score:
            totalWidth += self.numbers[digit].get_width()
        x = (self.screenWidth - totalWidth) // 2

        for digit in score:
            self.screen.blit(self.numbers[digit], (x, 100))
            x += self.numbers[digit].get_width()