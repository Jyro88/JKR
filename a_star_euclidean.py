import heapq
from node import Node
import math

# Literally same code as the other a* but with a different hueristic function
def a_star_euclidean(problem):
    initial_node = Node(state=problem.initial_state)
    if problem.goal_test(initial_node.state):
        return initial_node.path(), 1, 1
    
    frontier = []
    heapq.heappush(frontier, (initial_node.cost + initial_node.heuristic, initial_node))  
    explored = set()
    max_queue_size = 1

    while frontier:
        total_cost, node = heapq.heappop(frontier)
        explored.add(tuple(node.state))

        if problem.goal_test(node.state):
            return node.path(), max_queue_size, len(explored)

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            child_cost = node.cost + problem.step_cost(node.state, action)
            child_heuristic = heuristic_euclidean(child_state, problem.goal_state)  
            child_node = Node(state=child_state, parent=node, action=action, cost=child_cost, heuristic=child_heuristic)

            if tuple(child_state) not in explored:
                heapq.heappush(frontier, (child_node.cost + child_node.heuristic, child_node))
                explored.add(tuple(child_state))
                max_queue_size = max(max_queue_size, len(frontier))

    return None, max_queue_size, len(explored)

def heuristic_euclidean(state, goal_state):
    # Euclidean distance heuristic calculates the distance between each tile in the current state
    # and its goal position, then sums these distances.
    distance = 0
    for i in range(len(state)):
        if state[i] != 0:  # Exclude the blank tile
            current_row, current_col = i // 3, i % 3
            goal_index = goal_state.index(state[i])
            goal_row, goal_col = goal_index // 3, goal_index % 3
            distance += math.sqrt((current_row - goal_row) ** 2 + (current_col - goal_col) ** 2)
    return distance