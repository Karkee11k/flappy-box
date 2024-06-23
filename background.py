from pygame import SurfaceType

from settings import Settings

class Background:
    """A class to create the background of the screen."""

    def __init__(self, screen: SurfaceType, settings: Settings):
        """Initializes the background."""
        self.screen = screen
        self.images = settings.background()
        self.bgRect = self.images[0].get_rect()
        self.baseRect = self.images[1].get_rect()        

    def fillBack(self) -> None:
        """Fills the background in the screen."""
        bgWidth = self.bgRect.width
        for i in range(3):
            self.screen.blit(self.images[0], (i * bgWidth, 0)) 
        
    def fillBase(self) -> None:
        """Fills the base in the screen."""
        baseWidth = self.baseRect.width
        baseY = self.bgRect.bottom
        for i in range(3):
            self.screen.blit(self.images[1], (i * baseWidth, baseY))