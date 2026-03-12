import pygame
from grid import Grid
from tetrominos import *  # noqa: F403


class Game:
    def __init__(self, screen: pygame.Surface, game_grid: Grid):
        pygame.init()
        self.fps = 60
        self.screen = screen
        self.current_tetro = ZTetromino()  # noqa: F405
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_grid = game_grid
        self.time_delay = 1000
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, self.time_delay)

    def move_left(self):
        self.current_tetro.move(0, -1)
        if not self._is_inside():
            self.current_tetro.move(0, 1)

    def move_rigth(self):
        self.current_tetro.move(0, 1)
        if not self._is_inside():
            self.current_tetro.move(0, -1)

    def move_down(self):
        self.current_tetro.move(1, 0)
        if not self._is_inside():
            self.current_tetro.move(-1, 0)

    def rotate(self):
        self.current_tetro.rotate()
        if not self._is_inside():
            self.current_tetro.undo_rotation()

    def undo_rotation(self):
        self.current_tetro.undo_rotation()
        if not self._is_inside():
            self.current_tetro.rotate()

    def _is_inside(self):
        positions = self.current_tetro.get_positions()
        for position in positions:
            if not self.game_grid.is_inside(position.y, position.x):
                return False
        return True
