import argparse

my_parser = argparse.ArgumentParser(description="Coloring Game! Read README.md for more informations")

my_parser.add_argument('-r',
                       '--rows',
                       type = int,
                       default = 18,
                       help = "How many rows You want to be visible at board? By default: 18")
my_parser.add_argument('-c',
                       '--columns',
                       type = int,
                       default = 18,
                       help = "How many columns You want to be visible at board? By default: 18")
my_parser.add_argument('-rs',
                       '--rounds',
                       type = int,
                       default = 21,
                       help = "How many rounds You need to solve this game? By default: 21")
