import pygame


class Grid:
    def __init__(self) -> None:
        self.collumns = 10
        self.lines = 20
        self.cell_size = 40
        self.grid = [[0 for _ in range(self.collumns)] for _ in range(self.lines)]
        self.colors = self._get_colors()

    def output_grid(self) -> None:
        for line in range(self.lines):
            for collumn in range(self.collumns):
                print(self.grid[line][collumn], end=" ")
            print()

    def draw(self, screen):
        for line in range(self.lines):
            for collumn in range(self.collumns):
                color = self.grid[line][collumn]
                cell_rect = pygame.Rect(
                    line * self.cell_size + 1,
                    collumn * self.cell_size + 1,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, color, cell_rect)

    def _get_colors(self):
        gray = (146, 146, 146)
        blue = (4, 65, 174)
        green = (114, 203, 59)
        yellow = (255, 213, 4)
        orange = (255, 151, 29)
        red = (255, 50, 21)

        return [gray, blue, green, yellow, orange, red]
