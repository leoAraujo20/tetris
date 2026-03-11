import pygame
from grid import Grid
from tetrominos import *  # noqa: F403


class Game:
    def __init__(self):
        pygame.init()
        self.window_size = (400, 800)
        self.fps = 60
        self.screen = pygame.display.set_mode(self.window_size)
        self.current_tetro = ZTetromino()  # noqa: F405
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.game_grid = Grid()
        self.time_delay = 1000
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, self.time_delay)

    def run(self):
        while self.running:
            self.screen.fill("black")
            self.game_grid.draw(self.screen)
            self.current_tetro.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(self.game_grid.colors)
                    self.game_grid.output_grid()
                    self.running = False

                if event.type == self.timer_event:
                    self._move_down()

            keys = pygame.key.get_just_pressed()
            if keys[pygame.K_a]:
                self._move_left()
            if keys[pygame.K_d]:
                self._move_rigth()
            if keys[pygame.K_x]:
                self._rotate()
            if keys[pygame.K_z]:
                self._undo_rotation()

            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000

    def _move_left(self):
        self.current_tetro.move(0, -1)
        if not self._is_inside():
            self.current_tetro.move(0, 1)

    def _move_rigth(self):
        self.current_tetro.move(0, 1)
        if not self._is_inside():
            self.current_tetro.move(0, -1)

    def _move_down(self):
        self.current_tetro.move(1, 0)
        if not self._is_inside():
            self.current_tetro.move(-1, 0)

    def _rotate(self):
        self.current_tetro.rotate()

    def _undo_rotation(self):
        self.current_tetro.undo_rotation()

    def _is_inside(self):
        positions = self.current_tetro.get_positions()
        for position in positions:
            if not self.game_grid.is_inside(position.y, position.x):
                return False
        return True


Game().run()
pygame.quit()
