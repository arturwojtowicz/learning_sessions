from typing import Dict

from accessor_base import Colors


class Cell:
    """
    Each cell in a board has a representative instance of Cell. It stores data and communicates between neighbors
    """
    def __init__(self, color: Colors):
        self.previous_color = None
        self.color = color

    @property
    def color(self) -> Colors:
        """
        Returns:
            _color: Colors
        """
        return self._color

    def update_color(self, color: Colors):
        """
        Updating previous color that this instance has and current.
        """
        self.previous_color = self._color
        self.color = color

    @property
    def neighbors(self) -> Dict:
        """
        Returns:
            _neighbors
        """
        return self._neighbors

    def update_neighbors(self, neighbors: Dict):
        """
        Updating neigbors for current instance
        """
        self._neighbors = neighbors

    @property
    def run(self) -> str:
        """
        Returns:
            str: Colored block for board
        """
        return f"{self.color}   "

    def update(self, color: Colors):
        """
        Updating color of the current instance and notify neighbors if they needs to change as well, whenever they had same color at start.
        """
        self.update_color(color)
        for neighbor in self._neighbors.values():
            if neighbor != None and self._previous_color != neighbor.color:
                neighbor.update(color)
