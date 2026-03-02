import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.columns = 10
        self.rows = 20
        self.cell_size = 40
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.colors = Colors.get_colors()

    def output_grid(self) -> None:
        for row in range(self.rows):
            for Column in range(self.columns):
                print(self.grid[row][Column], end=" ")
            print()

    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                cell_pos = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size + 1,
                    row * self.cell_size + 1,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, self.colors[cell_pos], cell_rect)

    def is_inside(self, row, column) -> bool:
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return False
        return True
