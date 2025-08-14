from re import fullmatch
from math import floor
from decider import graph

def is_valid_format(s: str):
    pattern = r'^[A-Z0-9_-]+$'
    return fullmatch(pattern, s) is not None

if __name__ == "__main__":
    transition_table = input("Input the Turing Machine in Standard Text Format: ")
    d = int(input("Depth: "))
    if not is_valid_format(transition_table):
        print("Invalid format.")
        exit(1)
    segments = transition_table.split("_")
    if not segments:
        print("Empty machine code.")
        exit(1)
    for segment in segments:
        if len(segment) % 3 != 0:
                print("Invalid format.")
                exit(1)

    n = 1 # no. of states = (no. of underscores + 1)
    k = 0
    i = 0
    for char in transition_table:
        i += 1
        if char == "_":
            n += 1
            if n == 2: # n starts at 1.
                k = floor((i-1)/3)

    graph(n, k, transition_table, d)