from random import randint
from pygame import SurfaceType

from box import Box
from settings import Settings

class Pipe:
    """A class to represent the pipe."""
    
    def __init__(self, screen: SurfaceType, settings: Settings, pipeImage: tuple):
        """Initializes the pipe's attributes."""
        self.__screen = screen
        self.__velocity = settings.pipeVelocity
        self.__end = screen.get_rect().left
        self.count = 0

        # upper and the lower pipe images
        self.upperImage = pipeImage[0]
        self.lowerImage = pipeImage[1]        
        self.lowerRect = self.lowerImage.get_rect()
        self.upperRect = self.upperImage.get_rect()

        # choosing random pipes
        self.upperRect.top = randint(-180, 0)
        self.lowerRect.top = self.upperRect.bottom + settings.pipeGapSize

    def update(self) -> None:
        """Updates the pipe's movement."""
        self.upperRect.x += self.__velocity
        self.lowerRect.x += self.__velocity
    
    def disappeared(self) -> bool:
        """Returns true if the pipe disappeared from the screen."""
        return self.upperRect.left + self.upperRect.width < self.__end
    
    def boxCollided(self, box: Box) -> bool:
        """Returns true if the box hit the pipe."""
        if self.upperRect.colliderect(box.rect): return True
        return self.lowerRect.colliderect(box.rect)
    
    def boxCrossed(self, box: Box) -> bool:
        """Returns true if the box crossed the pipe."""
        return self.upperRect.right <= box.rect.left

    def draw(self) -> None:
        """Draws the pipe on the screen."""
        self.__screen.blit(self.upperImage, self.upperRect)
        self.__screen.blit(self.lowerImage, self.lowerRect)