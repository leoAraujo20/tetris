import pygame


class Grid:
    def __init__(self) -> None:
        self.collumns = 10
        self.lines = 20
        self.cell_size = 40
        self.grid = [[0 for _ in range(self.collumns)] for _ in range(self.lines)]

    def output_grid(self) -> None:
        for line in range(self.lines):
            for collumn in range(self.collumns):
                print(self.grid[line][collumn], end=" ")
            print()

    def draw(self, surface): ...
