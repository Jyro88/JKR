import heapq
from node import Node

def uniform_cost_search(problem):
    # initial node values: state, parent=None, action=None, cost=0, heuristic=0
    initial_node = Node(state=problem.initial_state)
    if problem.goal_test(initial_node.state):
        return initial_node.path(), 1, 1
    
    frontier = []
    # initialize frontier as a priority queue and push initial node
    heapq.heappush(frontier, initial_node)
    explored = set()
    max_queue_size = 1

    while frontier:
        # Pop node from frontier based on the node.cost starting with the initial node
        node = heapq.heappop(frontier)

        # Keep track of nodes we have expanded
        explored.add(tuple(node.state))

        # problem.actions finds all possible actions of the current state based on the position of the blank
        # The function is in problem.py and is pretty easy to follow
        for action in problem.actions(node.state):

            # Assign the child state to the resulting board after the action is carried out
            child_state = problem.result(node.state, action)

            # Cost is the cost of the current/parent node + the cost of taking the action, which is just 1
            # So the cost of each child is just increasing by 1 for each depth level
            child_cost = node.cost + problem.step_cost(node.state, action)
            child_node = Node(state=child_state, parent=node, action=action, cost=child_cost)
            
            if problem.goal_test(child_state):
                return child_node.path(), max_queue_size, len(explored)

            if tuple(child_state) not in explored:
                heapq.heappush(frontier, child_node)
                explored.add(tuple(child_state))
                max_queue_size = max(max_queue_size, len(frontier))

    return None, max_queue_size, len(explored)