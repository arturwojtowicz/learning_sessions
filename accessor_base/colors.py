import random

from colorama import Back, Style


class Colors:
    BLUE = Back.BLUE
    GREEN = Back.GREEN
    YELLOW = Back.YELLOW
    RED = Back.RED
    STOP = Style.RESET_ALL

    @staticmethod
    def random_color() -> Back:
        """
        Picks a random color

        Returns:
            Colors
        """
        return random.choice([Colors.BLUE, Colors.GREEN, Colors.YELLOW])

    @staticmethod
    def colors_mapping() -> Back:
        """
        Mapping for user entry for a color
        """
        return {
            "r": Colors.RED,
            "red": Colors.RED,
            "g": Colors.GREEN,
            "green": Colors.GREEN,
            "y": Colors.YELLOW,
            "yellow": Colors.YELLOW
        }
