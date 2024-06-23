import pygame
from collections import deque

from background import Background
from box import Box
from game_stats import GameStats
from min_pq import MinPQ
from pipe import Pipe
from score_board import Scoreboard
from settings import Settings


class GameTransition:
    """A class to control game logic in different game states."""

    def __init__(self, screen: pygame.SurfaceType, settings: Settings, stats: GameStats):
        """Initializes the game transition instance."""
        self.screen = screen
        self.stats = stats
        self.settings = settings
        self.scoreboard = Scoreboard(screen, settings, stats)
        self.newGame()

    
    def newGame(self) -> None:
        """Initializes the game objects needed for the new game."""
        self.background = Background(self.screen, self.settings)
        self.box = Box(self.screen, self.settings, self.background)
        self.pipeImage = self.settings.pipe()
        self.pipesQueue = deque()
        self.pq = MinPQ()
        self.stats.reset()
    

    def gameStart(self) -> None:
        """Sets up the game start screen (GET_READY transition)."""
        self.background.fillBack()
        self.background.fillBase()
        self.box.float()
        self.box.draw()
        self.scoreboard.drawGetReady()
        pygame.display.update()


    def runGame(self) -> None:
        """Runs the game (GAME_ACTIVE transition)."""
        self.box.update()
        self.updatePipes()
        self.background.fillBack()
        for pipe in self.pipesQueue: 
            pipe.draw()
        self.background.fillBase()
        self.box.draw()
        self.scoreboard.drawScore()
        self.checkCrash()
        pygame.display.update()


    def gameOver(self) -> None:
        """Shows the game over screen (GAME_OVER transition)."""
        if self.box.hitBase():
            self.stats.gameState = GameStats.END
        if self.stats.gameState != GameStats.END:
            self.box.update()
        self.background.fillBack()
        for pipe in self.pipesQueue: 
            pipe.draw()
        self.background.fillBase()
        self.box.draw()
        self.scoreboard.drawScore()
        self.scoreboard.drawGameOver()
        pygame.display.update()


    def checkCrash(self) -> None:
        """Sets the game state to GAME_OVER if player crashed."""

        # ground crash
        if self.box.hitBase():
            self.settings.sound['crash'].play()
            self.settings.sound['gameover'].play()
            self.stats.gameState = GameStats.GAME_OVER
            return
        
        pipe = self.pq.min() # pipe that the box going to cross

        # if crossed, update the score
        if pipe.boxCrossed(self.box):
            self.stats.score += 1
            self.settings.sound['score'].play()
            self.pq.delMin()
        
        # if crashed, move to game over transition
        elif pipe.boxCollided(self.box):
            self.settings.sound['crash'].play()
            self.settings.sound['gameover'].play()
            self.stats.gameState = GameStats.GAME_OVER


    def updatePipes(self) -> None:
        """Updates the pipes in the deque."""
        while len(self.pipesQueue) < self.settings.pipesAllowed:
            self.addPipe()

        if self.pipesQueue[0].disappeared(): 
            self.pipesQueue.popleft()

        for pipe in self.pipesQueue:
            pipe.update()


    def addPipe(self) -> None:
        """adds pipe to the deque and priority queue."""

        # if it is a first pipe
        if not self.pipesQueue:
            right = self.settings.screensize[0] + 30 
            count = 0
        else:
            right = self.pipesQueue[-1].upperRect.right + self.settings.pipesInterval 
            count = self.pipesQueue[-1].count + 1

        pipe = Pipe(self.screen, self.settings, self.pipeImage)
        pipe.count = count
        pipe.upperRect.right = right
        pipe.lowerRect.right = right
        self.pipesQueue.append(pipe) 
        self.pq.insert(pipe)