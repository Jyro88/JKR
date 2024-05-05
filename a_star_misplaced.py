import heapq
from node import Node

def a_star_misplaced(problem):    
    initial_node = Node(state=problem.initial_state)
    if problem.goal_test(initial_node.state):
        return initial_node.path(), 1, 1
    
    frontier = []
    heapq.heappush(frontier, (initial_node.cost + initial_node.heuristic, initial_node))  # Priority queue with (total_cost, node)
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
            child_heuristic = heuristic_misplaced_tiles(child_state, problem.goal_state)  # Calculate heuristic for child state
            child_node = Node(state=child_state, parent=node, action=action, cost=child_cost, heuristic=child_heuristic)

            if tuple(child_state) not in explored:
                heapq.heappush(frontier, (child_node.cost + child_node.heuristic, child_node))
                explored.add(tuple(child_state))
                max_queue_size = max(max_queue_size, len(frontier))

    return None, max_queue_size, len(explored)

def heuristic_misplaced_tiles(state, goal_state):
    misplaced = sum(1 for s, g in zip(state, goal_state) if s != g and s != 0)  # Exclude the blank tile from count
    return misplaced