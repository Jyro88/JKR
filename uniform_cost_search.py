import heapq
from node import Node

def uniform_cost_search(problem):
    initial_node = Node(state=problem.initial_state)
    if problem.goal_test(initial_node.state):
        return initial_node.path(), 1, 1
    
    frontier = []
    heapq.heappush(frontier, initial_node)
    explored = set()
    max_queue_size = 1

    while frontier:
        node = heapq.heappop(frontier)
        explored.add(tuple(node.state))

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            child_cost = node.cost + problem.step_cost(node.state, action)
            child_node = Node(state=child_state, parent=node, action=action, cost=child_cost)

            if problem.goal_test(child_state):
                return child_node.path(),  max_queue_size, len(explored)

            if tuple(child_state) not in explored:
                heapq.heappush(frontier, child_node)
                explored.add(tuple(child_state))
                max_queue_size = max(max_queue_size, len(frontier))
    return None, max_queue_size, len(explored)