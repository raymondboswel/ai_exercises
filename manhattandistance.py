

def calculate(state):
    goal_state = [[0,1,2],[3,4,5],[6,7,8]]
    total_distance = 0
    for row_num, row in enumerate(state):
        for col_num, num in enumerate(row):
            if num != 0:
                index = find_goal_num_index(num, goal_state)
                distance =  abs(index[0] - row_num) + abs(index[1] - col_num)
                total_distance = total_distance + distance
    return total_distance

def find_goal_num_index(num, state):
    row = -1
    col = -1
    n = len(state)
    for r in range(0, n):
        if state[r].count(num) == 1:
            row = r
            col = state[row].index(num)
    return (row, col)
