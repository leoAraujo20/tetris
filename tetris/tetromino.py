import pygame
from colors import Colors
from position import Position


class Tetromino:
    def __init__(self, id) -> None:
        self.id = id
        self.cell_size = 40
        self.cells = {}
        self.rotation_state = 0
        self.colors = Colors.get_colors()

    def _get_positions(self) -> list[Position]:
        blocks = self.cells[self.rotation_state]
        positions = []
        for block in blocks:
            positions.append(Position(*block))
        return positions

    def draw(self, screen):
        positions = self._get_positions()
        for position in positions:
            block_rect = pygame.Rect(
                position.x * self.cell_size + 1,
                position.y * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.colors[self.id], block_rect)
