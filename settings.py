from random import choice
import pygame

class Settings:
    """A class to store the settings for the game."""
    
    def __init__(self):
        """Initializes the game settings."""
        self.screensize = (800, 600)
        self.loadImage  = lambda path: pygame.image.load(path).convert_alpha()
        self.__loadSounds()

        # pipe settings
        self.pipeGapSize   = 100
        self.pipesAllowed  = 6
        self.pipeVelocity  = -4
        self.pipesInterval = 176
        
        # box settings
        self.boxMaxVelocity    = 15
        self.boxAcceleration   = 1
        self.flapAcceleration  = -9
        self.rotationVelocity  = 3
        self.rotationThreshold = 20

        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        """Initializes the settings that change throughout the game."""
        self.boxVelocity = -9
        self.boxRotation = 45

    def player(self) -> tuple:
        """Returns a random color player (red or blue or yellow)."""
        color = choice(['blue', 'red', 'yellow']) 
        down  = self.loadImage(f'images/{color}box-downflap.png')
        mid   = self.loadImage(f'images/{color}box-midflap.png')
        up    = self.loadImage(f'images/{color}box-upflap.png')
        return (down, mid, up)
    
    def pipe(self) -> tuple:
        """Returns a random color pipe (green or red)."""
        color = choice(['red', 'green'])
        lo = self.loadImage(f'images/pipe-{color}.png')
        up = pygame.transform.flip(lo, False, True)
        return (up, lo)

    def background(self) -> tuple:
        """Returns a random background (day or night)."""
        time = choice(['day', 'night'])
        bg   = self.loadImage(f'images/background-{time}.png')
        base = self.loadImage(f'images/base.png') 
        return (bg, base)
    
    def numbers(self) -> list:
        """Returns a list of numbers images from 0 to 9."""
        return [self.loadImage(f'images/{i}.png') for i in range(10)]
    
    def messages(self) -> tuple:
        """Returns the messages 'getready' and 'gameover'."""
        getready = self.loadImage('images/getready.png')
        gameover = self.loadImage('images/gameover.png')
        return (getready, gameover)

    def __loadSounds(self) -> None:
        """Loads the game sounds."""
        self.sound = {}
        self.sound['gameover'] = pygame.mixer.Sound('sounds/die.ogg')
        self.sound['crash']    = pygame.mixer.Sound('sounds/hit.ogg')
        self.sound['score']    = pygame.mixer.Sound('sounds/point.ogg')
        self.sound['flap']     = pygame.mixer.Sound('sounds/wing.ogg')