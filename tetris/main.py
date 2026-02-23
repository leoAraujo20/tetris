import pygame
from grid import Grid
from tetrominos import ITetromino


class Game:
    def __init__(self):
        pygame.init()
        self.window_size = (400, 800)
        self.fps = 60
        self.screen = pygame.display.set_mode(self.window_size)
        self.current_block = ITetromino()
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.game_grid = Grid()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(self.game_grid.colors)
                    self.game_grid.output_grid()
                    self.running = False

            self.screen.fill("black")
            self.game_grid.draw(self.screen)
            self.current_block.draw(self.screen)
            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000


Game().run()
pygame.quit()
