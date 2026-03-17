import random

import pygame
from grid import Grid
from tetromino import Tetromino
from tetrominos import *


class Game:
    def __init__(self, screen: pygame.Surface, game_grid: Grid):
        pygame.init()
        self.fps = 60
        self.screen = screen
        self.tetros = [
            ITetromino(),
            STetromino(),
            OTetromino(),
            LTetromino(),
            ZTetromino(),
        ]
        self.current_tetro = self._get_random_tetro()
        self.next_tetro = self._get_random_tetro()
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
            self._block_positions()
            self.current_tetro = self._get_random_tetro()

    def rotate(self):
        self.current_tetro.rotate()
        if not self._is_inside():
            self.current_tetro.undo_rotation()

    def undo_rotation(self):
        self.current_tetro.undo_rotation()
        if not self._is_inside():
            self.current_tetro.rotate()

    def _lock_positions(self):
        positions = self.current_tetro.get_positions()
        for position in positions:
            self.game_grid.grid[position.y][position.x] = self.current_tetro.id
        self.current_tetro = self.next_tetro
        self.next_tetro = self._get_random_tetro()

    def _is_inside(self):
        positions = self.current_tetro.get_positions()
        for position in positions:
            if not self.game_grid.is_inside(position.y, position.x):
                return False
        return True

    def _get_random_tetro(self) -> Tetromino:
        if len(self.tetros) == 0:
            self.tetros = [
                ITetromino(),
                STetromino(),
                OTetromino(),
                LTetromino(),
                ZTetromino(),
            ]
        tetro = random.choice(self.tetros)
        self.tetros.remove(tetro)
        return tetro
