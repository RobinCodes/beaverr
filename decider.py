from math import floor
from re import fullmatch
import string

"""
For machines with >9 symbols, the symbol used will have to remain a single character in order for the decider to work. (Due to STD)
"""

def is_valid_format(s: str):
    pattern = r'^[A-Z0-9_-]+$'
    return fullmatch(pattern, s) is not None

def read_transition_table(n: int, k: int, transition_table:str):
    segments = transition_table.split("_") #segment based on state
    if not segments:
        print("Empty machine code. [Invalid Format]")
        exit(1)
    
    transitions = []
    for segment in segments:
        if len(segment) % 3 != 0:
            print("Invalid format.")
            exit(1)
        for i in range(0, len(segment), 3):
            transition = segment[i:i+3]
            transitions.append(transition)

    j = 0 #used to keep track of the no. of transitions added to mapped_transitions

    pairs = []
    mapped_transitions = dict() #dictionary where we map the (state, symbol (currently transitions list)) -> WRITE,DIR,NEXT
    initial_transition = "A, 0"
    halting_transition = None
    for idx, letter in enumerate(string.ascii_uppercase):
        for number in range(0, k):
            if idx < n:
                pair = f"{str(letter)}, {str(number)}"
                pairs.append(pair)
                mapped_transitions[pair] = transitions[j]
                if transitions[j] == "---":
                    halting_transition = pair
                j += 1

    return mapped_transitions, pairs, initial_transition, halting_transition, transitions

def graph(n: int, k: int, transition_table: str, depth: int):
    """
    Function used to generate the graph with given depth.
    """
    print(f"Max. no. of configurations. {n*(k**2) - k}")
    print(read_transition_table(n, k, transition_table))
