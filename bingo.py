import argparse
import math
from random import choices, randint, choice, shuffle
import json
from itertools import permutations, combinations, islice
from random import sample



def generate_bingo_matrix(wordlist):
    size = int(math.sqrt(len(wordlist)))
    if size ** 2 != len(wordlist):
        raise ValueError("Wordlist has to be a multiple of 2")

    bingo = list()
    for i in range(size):
        bingo.append([None] * size)

    for i in range(size):
        for j in range(size):
            bingo[i][j] = wordlist[0]
            wordlist.remove(bingo[i][j])

    for row in bingo:
        print(row)
    return bingo

def generate_tex_string(matrix, template):

    data = []
    for row in matrix:
        data += row

    # Format the template with the data from the array
    formatted_template = template.format(*data)

    # Print or save the result
    # print(formatted_template)
    return formatted_template

def main():
    parser = argparse.ArgumentParser(description="A generator for Bingo cards")

    # Define named parameters
    parser.add_argument("-n", "--amount", type=int,
                        help="The number of Bingo cards that should be created", required=True)
    parser.add_argument("-p", "--path", type=str,
                        help="The path to a JSON File with all possible words in the Bingo game (at least size**2 words)",
                        required=True)
    parser.add_argument("-s", "--size", type=int,
                        help="The size of the Bingo game (one side of the square. default is 5 (5x5 Bingo)",
                        required=False, default=5)
    parser.add_argument("-o", "--out", type=str,
                        help="The path to store the generated tex file",
                        required=False, default="./bingo.tex")
    parser.add_argument("-t", "--template", type=str,
                        help="The path to tex template",
                        required=False, default="./tex_template_5x5.txt")
    # Parse arguments from command line
    args = parser.parse_args()

    # TODO defensive checks

    print(args)

    with open(args.template, 'r') as file:
        template_file = file.read()
    template = template_file.split("<-->")
    total = template[0]
    words = json.load(open(args.path))
    print("generating permutation and shuffle. This can take a while...")
    wordlists = islice(permutations(words, args.size**2), 0, args.amount, 100)
    # wordlists = shuffle(list(permutations(words, args.size**2)))
    counter = args.amount
    for i in range(args.amount):
        print(counter, flush=True)
        counter -= 1
        matrix = generate_bingo_matrix(sample(words, args.size**2))

        total += generate_tex_string(matrix, template[1])

        if counter <= 0: break

    total += f"\n{template[2]}"

    with open(args.out, 'w') as file:
        file.write(total)

    return





if __name__ == "__main__":
    main()
