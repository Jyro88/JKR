import heapq
from node import Node

def uniform_cost_search(problem):
    # Initialize an empty frontier (priority queue) to store nodes to be explored
    frontier = []
    # Initialize a set to store explored states
    explored = set()
    # Add the initial state node to the frontier with priority 0
    heapq.heappush(frontier, (0, Node(problem.initial_state)))
    
    # Continue searching until the frontier is empty
    while frontier:
        # Pop the node with the lowest cost from the frontier
        priority, node = heapq.heappop(frontier)
        # Extract the state from the node
        state = node.state
        
        # Check if the goal state is reached
        if problem.goal_test(state):
            # Return the goal node if found
            return node
        
        # Mark the current state as explored
        explored.add(tuple(state))
        
        # Generate child nodes for each possible action from the current state
        for action in problem.actions(state):
            # Get the resulting state after applying the action
            child_state = problem.result(state, action)
            # Calculate the cost of reaching the child node
            child_cost = node.cost + problem.step_cost(state, action)
            # Create a new node for the child state with updated cost and parent
            child_node = Node(child_state, node, action, child_cost)
            
            # Check if the child state has not been explored
            if tuple(child_state) not in explored:
                # Add the child node to the frontier with its cost as priority
                heapq.heappush(frontier, (child_cost, child_node))
    
    # Return None if no solution is found
    return None
