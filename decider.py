from math import floor
from re import fullmatch
import string

"""
For machines with >9 symbols, the symbol used will have to remain a single character in order for the decider to work.
"""

stop = False
checked_n = 0

def is_valid_format(s: str):
    pattern = r'^[A-Z0-9_-]+$'
    return fullmatch(pattern, s) is not None

def read_transition_table(n: int, k: int, transition_table:str):
    segments = transition_table.split("_") #segment based on state
    if not segments:
        print("Empty machine code.")
        exit(1)
    
    transitions = []
    for segment in segments:
        if len(segment) % 3 != 0:
            print("Invalid format.")
            exit(2)
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

def generate_connections(n: int, k: int, data):
    configurations = ['A, 0, 0, R']#state,symbol,symbol,direction
    for i in range(1, (n*(k**2) - k)+1):
        if i%k != 0 and data[4][floor(i/k)][1] == "-":
            continue
        elif i%k == 0 and data[4][floor(i/k)][1] == "-":
            configurations.append(f"{data[1][floor(i/k)]}, {0}")
        else:
            configurations.append(f"{data[1][floor(i/k)]}, {i%k}, {data[4][floor(i/k)][1]}")

    connections = dict()#map (configuration) -> (configuration_parents)(list)
    for _, config in enumerate(configurations):
        temp = list()
        config_data = config.split(",")
        config_transition = f"{config_data[0]},{config_data[1]}"
        for i in range(0, k):
            temp.append(f"{data[0][config_transition][-1]}, {config_data[2]}, {i}, {data[0][config_transition][-2]}")
        connections[config] = temp

    return configurations, connections

def check(branches: list, W: int):
    global checked_n, stop
    checked_n += 1
    
    pass
    #stop = True if depth (or time?) limit met
    #stop = True if solved
    if checked_n >= W+1:
        stop = True

def graph(n: int, k: int, transition_table: str, depth: int, rec_depth: int):
    """
    Function used to generate the graph with given depth.
    """
    print(f"Max. no. of configurations. {n*(k**2) - k}")
    
    data = read_transition_table(n, k, transition_table)
    configurations = generate_connections(n, k, data)#configurations[0] gives configs list, [1] connections
    branches = list() #list of branches generated, starting from C,0 and working our way backwards.
    #how this works: start at C,0 (halting_transition), seek all the ones that point to C,0. Then
    #continue the process, how to reach the ones that are required to reach C,0, etc
    rev_connections = dict()

    check(branches, rec_depth)


if __name__ == "__main__":
    TM = input("Input the Turing Machine in Standard Text Format: ")
    if not is_valid_format(TM):
        print("Invalid format.")
        exit(2)
    n = 1 # no. of states = (no. of underscores + 1)
    k = 0
    i = 0
    for char in TM:
        i += 1
        if char == "_":
            n += 1
            if n == 2: # n starts at 1.
                k = floor((i-1)/3)
    
    try:
        D = int(input("Initial depth: "))
        W = int(input("Additional depth: "))
        time_lim = int(input("Time limit: "))
        if D < 1 or W < 1 or time_lim < 1:
            print("Invalid values")
            exit(3)
    except ValueError:
        print("Invalid values")
        exit(3)

    graph(n, k, TM, D, W)
    if int(input("Continue with additional extensions? (0/1)")) == 1:
        while not stop:
            graph(n, k, TM, 1, W)
    #output_info() into a file
    exit(0)
    
# todo once complete: save to file if interrupted. add way to begin from where you left off