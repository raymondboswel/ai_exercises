import queue
import copy


class Node:
    def __init__(self, state, parent_node, action, depth):
        self.state = state
        self.parent_node = parent_node
        self. action = action
        # self.path_cost = path_cost
        self.depth = depth


# Fringe -> empty queue
def tree_search(initial ,fringe):
    initialNode = Node(initial, None, None, 0)
    found_solution = False
    x = 0
    fringe = insert(initialNode, fringe) #Adds the initial node in the queue
    while not found_solution:
        x = x + 1
        print("\nIteration: {}".format(x))
        print('=====================================================================')
        if fringe.empty():
            print("Solution not found")
            break
        node = make_node(fringe)
        print("Current state: {}".format(node.state))
        print("Previous action: {}".format(node.action))
        if is_goal_state(node):
            print("Found goal")
            found_solution = True
            break
        previous_states.append(node.state)
        fringe = insert_all(expand(node), fringe)
        print("Queue size: {}".format(fringe.qsize()))
    return "solution not found in allotted iterations"

def insert_all(successors, fringe):
    for successor in successors:
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
    actions = []
    zero_on_edge = False
    zero_index = find_zero_index(node.state)
    actions = ["swap_left", "swap_right", "swap_up", "swap_down"]
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
    print("Actions: {}".format(actions))
    print("Node.state: {}".format(node.state))
    successors = generate_successors(node.state, actions)

    return successors

def generate_successors(state, actions):
    successors = []
    print(state)
    zero_index = find_zero_index(state)
    print("Zero index: {}".format(zero_index))
    for action in actions:
        if action == "swap_up":
            swap_value_index = (zero_index[0]-1, zero_index[1])
            successor_state = copy.deepcopy(state)
            successor_state[zero_index[0]][zero_index[1]] = state[swap_value_index[0]][swap_value_index[1]]
            successor_state[swap_value_index[0]][swap_value_index[1]] = 0
            if is_not_repeat_state(successor_state):
                successors.append(("swap_up",successor_state))
        if action == "swap_down":
            swap_value_index = (zero_index[0]+1, zero_index[1])
            successor_state = copy.deepcopy(state)
            successor_state[zero_index[0]][zero_index[1]] = state[swap_value_index[0]][swap_value_index[1]]
            successor_state[swap_value_index[0]][swap_value_index[1]] = 0
            if is_not_repeat_state(successor_state):
                successors.append(("swap_down", successor_state))
        if action == "swap_left":
            swap_value_index = (zero_index[0], zero_index[1]-1)
            successor_state = copy.deepcopy(state)
            successor_state[zero_index[0]][zero_index[1]] = state[swap_value_index[0]][swap_value_index[1]]
            successor_state[swap_value_index[0]][swap_value_index[1]] = 0
            if is_not_repeat_state(successor_state):
                successors.append(("swap_left", successor_state))
        if action == "swap_right":
            swap_value_index = (zero_index[0], zero_index[1]+1)
            successor_state = copy.deepcopy(state)
            successor_state[zero_index[0]][zero_index[1]] = state[swap_value_index[0]][swap_value_index[1]]
            successor_state[swap_value_index[0]][swap_value_index[1]] = 0
            if is_not_repeat_state(successor_state):
                successors.append(("swap_right", successor_state))


    return successors

def is_not_repeat_state(successor_state):
    is_not_repeat_state = True
    for previous_state in previous_states:
        if successor_state == previous_state:
            is_not_repeat_state = False
    return is_not_repeat_state

def find_zero_index(state):
    row = -1
    col = -1
    for r in range(0, n-1):
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

def is_legal_action(node, action):
    new_state = apply_action(node.state, action)
    valid = True
    for key, value in new_state.items():
        if value < 0 :
            valid = False
    left_balance_ok = new_state['l_missionaries'] >= new_state['l_cannibals']
    right_balance_ok = new_state['r_missionaries'] >= new_state['r_cannibals']

    if (new_state ['l_missionaries'] != 0 and not left_balance_ok) or ((not right_balance_ok and new_state['r_missionaries']!=0)):
        valid = False
    for previous_state in previous_states:
        if new_state == previous_state:
            valid = False
    return valid

def apply_action(state, action):
    new_state = {}
    for key, value in action.items():
        new_state[key] = state[key] - value
    return new_state

def is_goal_state(node):
    if node.state == [[0, 1, 2], [3,4,5], [6,7,8]]:
        return True

def insert(element, queue):
    queue.put(element)
    return queue

def make_node(fringe):
    return fringe.get()

initial = [[1,2,5],[3,4,0],[6,7,8]]
n = 3

fringe = queue.Queue()
previous_states = []
tree_search(initial, fringe)