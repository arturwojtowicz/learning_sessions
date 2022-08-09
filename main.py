from typing import List

from accessor_base import Colors, my_parser
from board import Board


class ColoringGame:
    """
    Main handler of ColoringGame
    """
    def __init__(self, dimension: List, rounds: int):
        """
        Initializes Board

        Args:
            board: instance of Board
            rounds: rounds that player has to solve ColoringGame
        """
        self.board = Board(dimension)
        self.rounds = rounds

    def _game(self):
        """
        Game itself, it handles the colors passed by user and informs board, about needed update of color.
        """
        previous_color = self.board._cells[0][0].color
        available_colors = Colors.colors_mapping()

        for i in range(self.rounds):
            new_color = ""

            print(self.board.generate_map())
            while new_color.lower() not in available_colors.keys():
                new_color = input(f"Round {i}/{self.rounds}.\nSelect new color r (red) / b (blue) / y (yellow) / g (green): ")
                if new_color.lower() in Colors.colors_mapping() and available_colors[new_color.lower()] == previous_color:
                    new_color = ""

            self.board.update_colors(Colors.colors_mapping()[new_color])
            previous_color = Colors.colors_mapping()[new_color]

            if all([cell.color == self.board._cells[0][0].color for row in self.board._cells for cell in row]):
                print("Yayyy!! You won!!")
            else:
                print("Ooooopsie... Maybe try again?")

        print(self.board.generate_map())

    def run(self):
        """
        The game run itself, triggers map to be built
        """
        self.board.build_map()
        self._game()

        if all([cell.color == self.board._cells[0][0].color for row in self.board._cells for cell in row]):
            print("Yayyy!! You won!!")
        else:
            print("Ooooopsie... Maybe try again?")


if __name__ == '__main__':
    parser = my_parser.parse_args()

    dimension = [parser.columns, parser.rows]
    rounds = parser.rounds
    
    coloring_game = ColoringGame(dimension, rounds)
    coloring_game.run()
