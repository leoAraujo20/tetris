import random

import pygame
from grid import Grid
from tetromino import Tetromino
from tetrominos import *


class Game:
    def __init__(self, screen: pygame.Surface, game_grid: Grid):
        pygame.init()
        self.screen = screen
        self.tetros = [
            ITetromino(),
            STetromino(),
            OTetromino(),
            LTetromino(),
            ZTetromino(),
            TTetromino(),
            JTetromino(),
        ]
        self.game_grid = game_grid
        self.current_tetro = self._get_random_tetro()
        self.next_tetro = self._get_random_tetro()
        self.state = "playing"
        self.score = 0
        self.clock = pygame.time.Clock()
        self.time_delay = 500
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, self.time_delay)
        self.move_sound = pygame.mixer.Sound("sounds/Tetris (GB) (18)-move_piece.wav")
        self.rotate_sound = pygame.mixer.Sound(
            "sounds/Tetris (GB) (19)-rotate_piece.wav"
        )
        self.line_clear_sound = pygame.mixer.Sound(
            "sounds/Tetris (GB) (21)-line_clear.wav"
        )

    def reset(self):
        self.game_grid.clear()
        self.current_tetro = self._get_random_tetro()
        self.next_tetro = self._get_random_tetro()
        self.state = "playing"

    def move_left(self):
        self.move_sound.play()
        self.current_tetro.move(0, -1)
        if not self._is_inside() or self._has_collision():
            self.current_tetro.move(0, 1)

    def move_right(self):
        self.move_sound.play()
        self.current_tetro.move(0, 1)
        if not self._is_inside() or self._has_collision():
            self.current_tetro.move(0, -1)

    def move_down(self):
        self.move_sound.play()
        self.current_tetro.move(1, 0)
        if not self._is_inside() or self._has_collision():
            self.current_tetro.move(-1, 0)
            self._lock_positions()

    def rotate(self):
        self.rotate_sound.play()
        self.current_tetro.rotate()
        if not self._is_inside() or self._has_collision():
            self.current_tetro.undo_rotation()

    def undo_rotation(self):
        self.rotate_sound.play()
        self.current_tetro.undo_rotation()
        if not self._is_inside() or self._has_collision():
            self.current_tetro.rotate()

    def _lock_positions(self):
        positions = self.current_tetro.get_positions()
        for position in positions:
            self.game_grid.grid[position.y][position.x] = self.current_tetro.id
        cleared_rows = self.game_grid.clear_rows()
        if cleared_rows > 0:
            self.line_clear_sound.play()
            self.score += cleared_rows * 40
        self.current_tetro = self.next_tetro
        self.next_tetro = self._get_random_tetro()
        self.check_game_over()

    def _is_inside(self):
        positions = self.current_tetro.get_positions()
        for position in positions:
            if not self.game_grid.is_inside(position.y, position.x):
                return False
        return True

    def _has_collision(self):
        positions = self.current_tetro.get_positions()
        for position in positions:
            if self.game_grid.has_collison(position.y, position.x):
                return True
        return False

    def _get_random_tetro(self) -> Tetromino:
        if len(self.tetros) == 0:
            self.tetros = [
                ITetromino(),
                STetromino(),
                OTetromino(),
                LTetromino(),
                ZTetromino(),
                TTetromino(),
                JTetromino(),
            ]
        tetro = random.choice(self.tetros)
        self.tetros.remove(tetro)
        return tetro

    def draw_next_tetro(self, screen):
        if self.next_tetro.id == 3:
            self.next_tetro.draw(screen, 350, 310)
        elif self.next_tetro.id == 1:
            self.next_tetro.draw(screen, 350, 330)
        else:
            self.next_tetro.draw(screen, 370, 310)

    def check_game_over(self):
        if self._has_collision():
            self.state = "game_over"
