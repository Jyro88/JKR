import math
import time
from node import Node  # Assuming the node definition is in node.py
from problem import Problem  # Assuming the problem setup is in problem.py

def euclidean_distance(state1, state2):
    return math.sqrt(sum((s1 - s2) ** 2 for s1, s2 in zip(state1, state2)))

def a_star_euclidean(problem):
    start_node = Node(state=problem.initial_state)
    frontier = [start_node]  # Typically, a priority queue should be used
    frontier_size = 1  # Track maximum size of the frontier
    nodes_expanded = 0  # Track number of nodes expanded
    explored = set()
    
    while frontier:
        # Updating the maximum frontier size
        frontier_size = max(frontier_size, len(frontier))

        # Sorting to get the node with the lowest f(n) = g(n) + h(n)
        frontier.sort(key=lambda node: node.cost + euclidean_distance(node.state, problem.goal_state))
        current_node = frontier.pop(0)

        nodes_expanded += 1
        
        if problem.goal_test(current_node.state):
            return current_node, frontier_size, nodes_expanded
        
        explored.add(tuple(current_node.state))
        
        for action in problem.actions(current_node.state):
            child = current_node.child_node(problem, action)
            if tuple(child.state) not in explored:
                if child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    # Find the node and possibly update path_cost
                    index = frontier.index(child)
                    if child.cost < frontier[index].cost:
                        frontier[index] = child
    
    return None  # If no solution found


