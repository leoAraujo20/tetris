from tetromino import Tetromino


class ITetromino(Tetromino):
    def __init__(self, id=1) -> None:
        super().__init__(id)
        self.cells = {
            0: [(0, 0), (0, 1), (0, 2), (0, 3)],
        }
