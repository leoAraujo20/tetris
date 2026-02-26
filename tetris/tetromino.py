import pygame
from colors import Colors
from position import Position


class Tetromino:
    def __init__(self, id) -> None:
        self.id = id
        self.cell_size = 40
        self.cells = {}
        self.rotation_state = 0
        self.row_offset = 3
        self.column_offset = 5
        self.colors = Colors.get_colors()

    def _get_positions(self) -> list[Position]:
        blocks = self.cells[self.rotation_state]
        positions = []
        for position in blocks:
            positions.append(
                Position(position.x + self.column_offset, position.y + self.row_offset)
            )
        return positions

    def draw(self, screen) -> None:
        positions = self._get_positions()
        for position in positions:
            block_rect = pygame.Rect(
                position.x * self.cell_size + 1,
                position.y * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.colors[self.id], block_rect)

    def move(self, rows, columns) -> None:
        self.row_offset += rows
        self.column_offset += columns
