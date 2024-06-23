import pygame
from itertools import cycle

from background import Background
from settings import Settings

class Box:
    """A class to represent the box."""

    def __init__(self, screen: pygame.SurfaceType, settings: Settings, bg: Background):
        """Initializes the box's attributes."""
        self._images = settings.player()
        self.rect = self._images[0].get_rect()
        self.rect.center = screen.get_rect().center
        self.rect.x = self.rect.centerx - 150
        self.flapped = False

        self._screen = screen 
        self._settings = settings
        self._bottom = bg.bgRect.bottom
        self._cache = [{}, {}, {}]
        self._image = self._images[0]
        self._cycle = cycle([0, 1, 2, 1])
        self._index = self._iter = 0
        self._height = self._images[0].get_height()
        self._centery = self.y = self.rect.y
        self._direction = -1


    def float(self) -> None:
        """Makes the box float."""
        if abs(self.rect.y - self._centery) > 7:
            self._direction *= -1
        self.rect.y += self._direction
        self._changeWings()
        self._image = self._images[self._index]


    def update(self) -> None:
        """Updates the box's position."""
        self._changeWings()
        self._increaseVelocity()
        if self.flapped: self._flap()
        self._rotate()
        self.y += min(self._settings.boxVelocity, self._bottom - self._height - self.y)
        self.rect.y = max(0, self.y)


    def hitBase(self) -> bool:
        """Returns true if box hit the base, else false."""
        return self.y + self._height >= self._bottom


    def draw(self) -> None:
        """Draws the box on the screen."""
        self._screen.blit(self._image, self.rect)


    def _rotate(self) -> None:
        """Rotates the box."""
        if self._settings.boxRotation > -90:
            self._settings.boxRotation -= self._settings.rotationVelocity
        angle = min(self._settings.boxRotation, self._settings.rotationThreshold)

        # caching the image and rect
        if angle not in self._cache[self._index]:
            image = pygame.transform.rotate(self._images[self._index], angle)
            rect = image.get_rect()
            rect.x = self.rect.x
            self._cache[self._index][angle] = (image, rect)
        
        self._image = self._cache[self._index][angle][0]
        self.rect = self._cache[self._index][angle][1]
    

    def _changeWings(self) -> None:
        """Changes the wings on every 5th iteration."""
        if (self._iter + 1) % 5 == 0:
            self._index = next(self._cycle)
        self._iter = (self._iter + 1) % 30


    def _increaseVelocity(self) -> None:
        """Increases the box velocity."""
        if self.flapped: return
        if self._settings.boxVelocity < self._settings.boxMaxVelocity:
            self._settings.boxVelocity += self._settings.boxAcceleration


    def _flap(self) -> None:
        """Flaps the bird."""
        self._settings.boxVelocity = self._settings.flapAcceleration
        self._settings.sound['flap'].play()
        self._settings.boxRotation = 45
        self.flapped = False