import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window_size = (400, 800)
        self.fps = 60
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.cell_default_color = (0, 0, 0)
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
        self.gravity_delay = 1
        self.delay_timer = 0
        self.board_array = [
            [self.cell_default_color for _ in range(self.board_collumns)]
            for _ in range(self.board_lines)
        ]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")

            keys = pygame.key.get_just_pressed()
            self._move_left_rigth(keys)

            self._draw_board()
            self._apply_gravity()
            self._draw_block()
            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000

    def _draw_board(self):
        for i in range(self.board_lines):
            self.cell.y = self.cell_size * i
            for j in range(self.board_collumns):
                self.cell.x = self.cell_size * j
                pygame.draw.rect(self.screen, self.board_array[i][j], self.cell)

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
        self.delay_timer += self.dt

        if self.delay_timer >= self.gravity_delay:
            self.delay_timer = 0
            x_update = int(self.block.x / self.cell_size)
            y_update = int(self.block.y / self.cell_size)

            if self.block.y < self.screen.get_height() - self.cell_size:
                self.block.y += self.cell_size
                next_y = int(self.block.y / self.cell_size)
                if self.board_array[next_y][x_update] == (255, 0, 0):
                    self.block.x = 0
                    self.block.y = 0
                    self.board_array[y_update][x_update] = (255, 0, 0)
            else:
                y_update = int(self.block.y / self.cell_size)
                self.block.x = 0
                self.block.y = 0
                self.board_array[y_update][x_update] = (255, 0, 0)


Game().run()
pygame.quit()
