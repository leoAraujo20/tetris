import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.collumns = 10
        self.lines = 20
        self.cell_size = 40
        self.grid = [[0 for _ in range(self.collumns)] for _ in range(self.lines)]
        self.colors = Colors.get_colors()

    def output_grid(self) -> None:
        for line in range(self.lines):
            for collumn in range(self.collumns):
                print(self.grid[line][collumn], end=" ")
            print()

    def draw(self, screen):
        for line in range(self.lines):
            for collumn in range(self.collumns):
                cell_pos = self.grid[line][collumn]
                cell_rect = pygame.Rect(
                    collumn * self.cell_size + 1,
                    line * self.cell_size + 1,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, self.colors[cell_pos], cell_rect)
