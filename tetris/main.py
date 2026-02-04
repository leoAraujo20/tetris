import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window_size = (400, 800)
        self.fps = 60
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
        self.gravity_timer = 0
        self.gravity_delay = 0.5  # Tempo em segundos entre cada queda de célula

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")

            keys = pygame.key.get_just_pressed()
            self._move_left_rigth(keys)

            self._draw_board()
            self._draw_block()
            self._apply_gravity()

            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000

    def _draw_board(self):
        for i in range(self.board_lines):
            for j in range(self.board_collumns):
                pygame.draw.rect(self.screen, "green", self.cell, 1)
                self.cell.x = self.cell_size * j
            self.cell.y = self.cell_size * i

    def _draw_block(self):
        pygame.draw.rect(self.screen, "red", self.block)

    def _move_left_rigth(self, keys):
        if keys[pygame.K_a]:
            if self.block.x > 0:
                self.block.x -= self.cell_size
        if keys[pygame.K_d]:
            if self.block.x < 340:
                self.block.x += self.cell_size

    def _apply_gravity(self):
        if self.block.y < self.screen.get_height() - self.cell_size:
            self.block.y += 100 * self.dt


Game().run()
pygame.quit()
