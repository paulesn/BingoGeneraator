# BingoGenerator

usage: bingo.py [-h] -n AMOUNT -p PATH [-s SIZE] [-o OUT] [-t TEMPLATE]

A generator for Bingo cards

options:

  -h, --help            show this help message and exit
  
  -n AMOUNT, --amount AMOUNT
                        The number of Bingo cards that should be created
                        
  -p PATH, --path PATH  The path to a JSON File with all possible words in the Bingo game (at least size**2 words)
  
  -s SIZE, --size SIZE  The size of the Bingo game (one side of the square. default is 5 (5x5 Bingo)
  
  -o OUT, --out OUT     The path to store the generated tex file
  
  -t TEMPLATE, --template TEMPLATE
                        The path to tex template
