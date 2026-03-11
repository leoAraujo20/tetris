from position import Position
from tetromino import Tetromino


class ITetromino(Tetromino):
    def __init__(self, id=1) -> None:
        super().__init__(id)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            3: [Position(0, 0), Position(1, 0), Position(2, 0), Position(3, 0)],
        }

        self.move(0, 3)


class STetromino(Tetromino):
    def __init__(self, id=2):
        super().__init__(id)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)],
        }
        self.move(0, 3)


class OTetromino(Tetromino):
    def __init__(self, id=3):
        super().__init__(id)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        }
        self.move(0, 3)


class LTetromino(Tetromino):
    def __init__(self, id=4):
        super().__init__(id)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)],
        }
        self.move(0, 3)


class ZTetromino(Tetromino):
    def __init__(self, id=5):
        super().__init__(id)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(1, 0), Position(2, 0)],
        }
        self.move(0, 3)
