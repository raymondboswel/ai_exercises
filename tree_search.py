import queue



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
    fringe = insert(initialNode, fringe) #Adds the initial node in the queue
    for x in range (0, 100000):
        print("\n Iteration: {}".format(x))
        print('=====================================================================')
        if fringe.empty():
            print("Solution not found")
            break
        node = make_node(fringe)
        if is_goal_state(node):
            print("Found goal")
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
    action = {'l_cannibals': -2, 'l_missionaries': 0, 'l_boat': -1, 'r_cannibals': 2, 'r_missionaries': 0, 'r_boat': 1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': -1, 'l_missionaries': -1, 'l_boat': -1, 'r_cannibals': 1, 'r_missionaries': 1, 'r_boat': 1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': 0, 'l_missionaries': -2, 'l_boat': -1, 'r_cannibals': 0, 'r_missionaries': 2, 'r_boat': 1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': -1, 'l_missionaries': 0, 'l_boat': -1, 'r_cannibals': 1, 'r_missionaries': 0, 'r_boat': 1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': 0, 'l_missionaries': -1, 'l_boat': -1, 'r_cannibals': 0, 'r_missionaries': 1, 'r_boat': 1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': 2, 'l_missionaries': 0, 'l_boat': 1, 'r_cannibals': -2, 'r_missionaries': 0, 'r_boat': -1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': 1, 'l_missionaries': 1, 'l_boat': 1, 'r_cannibals': -1, 'r_missionaries': -1, 'r_boat': -1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': 0, 'l_missionaries': 2, 'l_boat': 1, 'r_cannibals': 0, 'r_missionaries': -2, 'r_boat': -1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': 1, 'l_missionaries': 0, 'l_boat': 1, 'r_cannibals': -1, 'r_missionaries': 0, 'r_boat': -1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    action = {'l_cannibals': 0, 'l_missionaries': 1, 'l_boat': 1, 'r_cannibals': 0, 'r_missionaries': -1, 'r_boat': -1}
    if is_legal_action(node, action):
        result = apply_action(node.state, action)
        successors.append((action, result))
    return successors

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
    if node.state == {'l_cannibals': 0, 'l_missionaries': 0, 'l_boat': 0, 'r_cannibals': 3, 'r_missionaries': 3, 'r_boat': 1}:
        return True

def insert(element, queue):
    queue.put(element)
    return queue

def make_node(fringe):
    return fringe.get()

initial = {'l_cannibals': 3, 'l_missionaries': 3, 'l_boat': 1, 'r_cannibals': 0, 'r_missionaries': 0, 'r_boat': 0}
fringe = queue.Queue()
previous_states = []
tree_search(initial, fringe)