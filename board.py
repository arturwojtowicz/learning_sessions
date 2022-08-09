from typing import Dict, List

from accessor_base import Colors
from cell import Cell


class Board:
    """
    Main game board

    Attributes:
        _cells: Stores nested lists of Cell instances in 2D.
    """
    _cells = []

    def __init__(self, dimension: List):
        self.dimension = dimension

    def build_map(self):
        """
        Builds a map and creates instances of random colored Cells
        """
        for _ in range(self.dimension[1]):
            row = []
            for _ in range(self.dimension[0]):
                row.append(Cell(color = Colors.random_color()))
            self._cells.append(row)

        self.define_neighbors()

    def _find_neighbor(self, row: int, column: int) -> Cell:
        """
        Searching for Cell based on row and column passed

        Returns:
            Cell if found, None otherwise.
        """
        if 0 <= row < self.dimension[1] and 0 <= column < self.dimension[0]:
            return self._cells[row][column]
        return None

    def _mapping_neighbors(self, row: int, column: int) -> Dict:
        """
        Maps neighbors location
        """
        return {
            "up": self._find_neighbor(row - 1, column),
            "down": self._find_neighbor(row + 1, column),
            "left": self._find_neighbor(row, column - 1),
            "right": self._find_neighbor(row, column + 1)
        }

    def define_neighbors(self):  # Finish atm. Next session from there
        """
        Iterating over Cell instances and updating their neighbors
        """
        for row in range(len(self._cells)):
            for column in range(len(self._cells[row])):
                self._cells[row][column].update_neighbors(self._mapping_neighbors(row, column))

    def generate_map(self) -> str:
        """
        Generating map based on data gathered from cells

        Returns:
            String representative of colored map.
        """
        game_map = ""
        for row_cells in self._cells:
            for cell in row_cells:
                game_map += cell.run
            game_map += f"{Colors.STOP}\n"
        return game_map

    def update_colors(self, color: Colors):
        """
        Updating first cell, which going to inform others about color change
        """
        self._cells[0][0].update(color)
