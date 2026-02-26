from position import Position
from tetromino import Tetromino


class ITetromino(Tetromino):
    def __init__(self, id=1) -> None:
        super().__init__(id)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3)],
            1: [Position(0, 0), Position(1, 0), Position(2, 0), Position(3, 0)],
        }
