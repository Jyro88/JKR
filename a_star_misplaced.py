import heapq
from node import Node

def a_star_misplaced(problem):
    # Counts how many tiles are misplaced by comparing each value of the problem state to the goal state
    def misplaced_tiles(state):
        misplaced = 0
        for i in range(len(state)):
            if state[i] != problem.goal_state[i]:
                misplaced += 1
        return misplaced

    # Initialize an empty frontier (priority queue) to store nodes to be explored
    frontier = []
    # Initialize a set to store explored states
    explored = set()
    # Enqueue the initial state node into the frontier with a priority of 0 + h(n)
    initial_node = Node(problem.initial_state, cost=0, heuristic=misplaced_tiles(problem.initial_state))
    heapq.heappush(frontier, initial_node)
    frontier_size = 1  # Initialize frontier size
    
    # Continue searching until the frontier is empty
    while frontier:
        # Dequeue the node with the lowest cost + heuristic value from the frontier
        node = heapq.heappop(frontier)
        state = node.state
        
        # Check if the current state is the goal state
        if state == problem.goal_state:
            # Return the solution path if found
            solution_path = []
            while node:
                solution_path.append(node)
                node = node.parent
            return solution_path, frontier_size
        
        # Mark the current state as explored
        explored.add(tuple(state))
        
        # Generate child states for the current state
        for action in problem.actions(state):
            child_state = problem.result(state, action)
            # Calculate the cost of reaching the child state
            cost = node.cost + problem.step_cost(state, action)
            # Calculate the heuristic value for the child state
            heuristic_value = misplaced_tiles(child_state)
            # Create a child node
            child_node = Node(child_state, parent=node, action=action, cost=cost, heuristic=heuristic_value)
            
            # Check if the child state has not been explored
            if tuple(child_state) not in explored:
                # Enqueue the child node into the frontier with priority = total cost + heuristic value
                heapq.heappush(frontier, child_node)
                frontier_size += 1  # Increment frontier size
    
    # Return None if no solution is found
    return None, frontier_size
