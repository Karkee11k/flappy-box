class GameStats:
    """A class to store the game stats."""
    GET_READY, ACTIVE = 0, 1
    GAME_OVER, END    = 2, 3

    def __init__(self):
        """Initialize the game stats."""
        self.reset()
    
    def reset(self) -> None:
        """Resets the game stats."""
        self.gameState = GameStats.GET_READY
        self.score = 0