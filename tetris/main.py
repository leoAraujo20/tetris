import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window_size = (400, 800)
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.position_y = 0
        self.position_x = 0
        self.board_collumns = 10
        self.board_lines = 20
        self.cell_size = self.screen.get_width() / self.board_collumns
        self.cell = pygame.Rect(
            self.position_x, self.position_y, self.cell_size, self.cell_size
        )
        self.block = pygame.Rect(
            self.position_x, self.position_y, self.cell_size, self.cell_size
        )
        self.dt = 0

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                if self.block.y > 0:
                    self.block.y -= self.cell_size
            if keys[pygame.K_s]:
                if self.block.y < 760:
                    self.block.y += self.cell_size
            if keys[pygame.K_a]:
                if self.block.x > 0:
                    self.block.x -= self.cell_size
            if keys[pygame.K_d]:
                if self.block.x < 340:
                    self.block.x += self.cell_size

            self._draw_board()
            self._draw_block()

            pygame.display.flip()
            self.dt = self.clock.tick(60)

    def _draw_board(self):
        self.cell.y = 0
        for _ in range(self.board_lines):
            for _ in range(self.board_collumns):
                pygame.draw.rect(self.screen, "green", self.cell, 1)
                self.cell.x += self.cell_size
            self.cell.y += self.cell_size
            self.cell.x = 0

    def _draw_block(self):
        pygame.draw.rect(self.screen, "red", self.block)


Game().run()
pygame.quit()
