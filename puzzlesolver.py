import queue
import copy
import manhattandistance
import sys
import math

n = 3

class Node:
    def __init__(self, state, parent_node, action, depth):
        self.state = state
        self.parent_node = parent_node
        self. action = action
        # self.path_cost = path_cost
        self.depth = depth
    def __lt__(self, other):
        selfAction = self.action
        otherAction = other.action
        if selfAction == "swap_right":
            return True
        if selfAction == "swap_left" and otherAction != "swap_right":
            return True
        if selfAction == "swap_down" and otherAction != "swap_up":
            return False
        if selfAction == "swap_up":
            return False



# Fringe -> empty queue
def tree_search(initial ,fringe, search_type):
    solutions = []
    initialNode = Node(initial, None, None, 0)
    found_solution = False
    x = 0
    fringe = insert(initialNode, fringe) #Adds the initial node in the queue
    expanded_nodes = []
    branches_fully_explored = 0
    while not fringe.empty() and x < 20:
        x = x + 1
        print("\nIteration: {}".format(x))
        print('=====================================================================')
        print("\nBranches fully explored: {}".format(branches_fully_explored))
        if fringe.empty():
            print("Solution not found")
            break
        node = make_node(fringe)
        print("Current state: ")
        print(node.state[0])
        print(node.state[1])
        print(node.state[2])
        print("Depth: {}".format(node.depth))
        print("Previous action: {}".format(node.action))
        if is_goal_state(node.state):
            print("Found goal")
            print(get_path(node, []))
            found_solution = True
            solutions.append(node)
        previous_states.append(node.state)
        successors = expand(node)
        expanded_nodes.append(node)
        if search_type == "dfs":
            if not successors:
                # No successors, delete expanded ancestors
                branches_fully_explored = branches_fully_explored + 1
                for node in expanded_nodes:
                    node = None

        fringe = insert_all(successors, fringe, search_type)
        print("Queue size: {}".format(fringe.qsize()))
    for node in solutions:
        print(get_path(node, []))
    return "solution not found in allotted iterations"

def get_path(node, path_to_goal):
    print("Depth: {}".format(node.depth))
    print("Action: {}".format(node.action))
    print("State: {}".format(node.state))
    path_to_goal.append(node.action)
    if(node.parent_node != None):
        return get_path(node.parent_node, path_to_goal)
    else:
        print(path_to_goal)
        path_to_goal.reverse()
        return path_to_goal

def insert_all(successors, fringe, search_type):
    for successor in successors:
        if search_type == "ast":
            distance = manhattandistance.calculate(successor.state)
            fringe.put(successor, distance)
        else:
            fringe.put(successor)
    return fringe

def expand(node):
    successors = []
    for (action, result) in successor_fns(node):
        s = Node(result, node, action, node.depth + 1 )
        successors.append(s)
    print("successors")
    for successor in successors:
        print(successor.state)
    print("successors end")
    return successors


def successor_fns(node):
    successors = []
    actions = generate_legal_actions(node.state)
    print("Actions: {}".format(actions))
    print("Node.state: {}".format(node.state))
    actions.reverse()
    successors = generate_successors(node.state, actions)

    return successors

def generate_legal_actions(state):
    actions = ["swap_up", "swap_down", "swap_left", "swap_right"  ]
    zero_index = find_zero_index(state)
    print("zero index")
    print(zero_index)
    if zero_index[0] == 0:
        # zero in top row
        actions.remove("swap_up")
    if zero_index[0] == n-1:
        # zero in bottom row
        actions.remove("swap_down")
    if zero_index[1] == 0:
        # Zero in left column
        actions.remove("swap_left")
    if zero_index[1] == n-1:
        #  Zero index in right column
        actions.remove("swap_right")
    return actions

def generate_successors(state, actions):
    successors = []
    print(state)
    zero_index = find_zero_index(state)
    print("Zero index: {}".format(zero_index))
    for action in actions:
        if action == "swap_up":
            successor_state = swap_up(zero_index, state)
            if is_not_repeat_state(successor_state):
                successors.append(("swap_up",successor_state))
        if action == "swap_down":
            successor_state = swap_down(zero_index, state)
            if is_not_repeat_state(successor_state):
                successors.append(("swap_down", successor_state))
        if action == "swap_left":
            successor_state = swap_left(zero_index, state)
            if is_not_repeat_state(successor_state):
                successors.append(("swap_left", successor_state))
        if action == "swap_right":
            successor_state = swap_right(zero_index, state)
            if is_not_repeat_state(successor_state):
                successors.append(("swap_right", successor_state))
    return successors


def swap_left(zero_index, state):
    swap_value_index = (zero_index[0], zero_index[1]-1)
    print(swap_value_index)
    print(state)
    successor_state = swap(zero_index, swap_value_index, state)
    return successor_state

def swap_right(zero_index, state):
    swap_value_index = (zero_index[0], zero_index[1]+1)
    successor_state = swap(zero_index, swap_value_index, state)
    return successor_state

def swap_up(zero_index, state):
    swap_value_index = (zero_index[0]-1, zero_index[1])
    successor_state = swap(zero_index, swap_value_index, state)
    return successor_state

def swap_down(zero_index, state):
    swap_value_index = (zero_index[0]+1, zero_index[1])
    successor_state = swap(zero_index, swap_value_index, state)
    return successor_state

def swap(zero_index ,swap_value_index, state):
    successor_state = copy.deepcopy(state)
    successor_state[zero_index[0]][zero_index[1]] = state[swap_value_index[0]][swap_value_index[1]]
    successor_state[swap_value_index[0]][swap_value_index[1]] = 0
    return successor_state

def is_not_repeat_state(successor_state):
    is_not_repeat_state = True
    for previous_state in previous_states:
        if states_are_equal(previous_state, successor_state):
            is_not_repeat_state = False
    return is_not_repeat_state

def states_are_equal(s1, s2):
    shared_rows = 0
    for row in s1:
        shared_rows = shared_rows + s2.count(row)
    if shared_rows == len(s1):
        print('!!!!!!!!!!!!!!!!!!!!!!!found repeated state!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return True
    else:
        return False


def find_zero_index(state):
    row = -1
    col = -1
    for r in range(0, n):
        if state[r].count(0) == 1:
            row = r
            col = state[row].index(0)
    return (row, col)


def row_contains_zero(row):
    print("Checking row: {}".format(row))
    has_zero = False
    for i in row:
        print(i)
        if i == 0:
            has_zero = True
    return has_zero

def column_contains_zero(state, column):
    has_zero = False
    for row in state:
        if row[column] == 0:
            has_zero = True
    return has_zero

def is_goal_state(state):
    if states_are_equal(state, [[0, 1, 2], [3,4,5], [6,7,8]]):
        return True

def insert(element, queue):
    queue.put(element)
    return queue

def make_node(fringe):
    return fringe.get()


def get_search_type():
    search_type = sys.argv[1]
    return search_type

def get_puzzle_dimension(blocks):
    total_blocks = len(blocks)
    dim = math.sqrt(total_blocks)
    return int(dim)

def create_fringe(search_type):
    if search_type == "dfs":
        print("DFS")
        fringe = queue.LifoQueue()
    elif search_type == "bfs":
        print("BFS")
        fringe = queue.Queue()
    else:
        print("astar")
        fringe == queue.PriorityQueue()
    return fringe

def create_initial_state(blocks, dimension):
    initial_state = []
    blocks.reverse()
    for i in range(0, dimension):
        print(i)
        row = []
        for i in range(0, dimension):
            block = blocks.pop()
            row.append(block)
        initial_state.append(row)
    return initial_state

def get_blocks(raw_input):
    return raw_input.split(",")


initial = [[1,2,5],[3,4,0],[6,7,8]]
blocks = get_blocks(sys.argv[2])

n = get_puzzle_dimension(blocks)

initial_state = create_initial_state(blocks, n)

previous_states = []
search_type = get_search_type()
fringe = create_fringe(search_type)
print(search_type)
print(n)

tree_search(initial, fringe, search_type)

