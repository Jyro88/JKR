from problem import Problem
from uniform_cost_search import uniform_cost_search
from a_star_misplaced import a_star_misplaced
import time

def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(map(str, state[i:i+3])))

print("Welcome to JKR 8 puzzle solver.")
print("Type '1' to use a default puzzle, or '2' to enter your own puzzle:")
choice = int(input())

if choice == 1:
    initial_state = [1, 2, 3, 4, 8, 0, 7, 6, 5]
else:
    print("Enter your puzzle, use a zero to represent the blank")
    initial_state = []
    for i in range(3):
        row = input(f"Enter the {i+1} row, use space or tabs between numbers: ").split()
        initial_state.extend(map(int, row))

print("Enter your choice of algorithm:")
print("1. Uniform Cost Search")
print("2. A* with the Misplaced Tile heuristic")
print("3. A* with the Euclidean distance heuristic")
algorithm_choice = int(input())

# CPU TIME STARTS
start_cpu_time = time.process_time()

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
problem = Problem(initial_state, goal_state)

if algorithm_choice == 1:
    solution_node, frontier_size, nodes_expanded = uniform_cost_search(problem)
elif algorithm_choice == 2:
    solution_node, frontier_size, nodes_expanded = a_star_misplaced(problem)
# elif algorithm_choice == 3:
#     solution_node = a_star_euclidean(problem)
else:
    print("Invalid choice of algorithm.")
    exit()

if solution_node:
    # UCS Trace
    if algorithm_choice == 1:
        # Print the solution path
        for i, node in enumerate(solution_node):
            print(f"State {i+1}:")
            print_state(node.state)
            print("")
            # If an action was taken, print the direction the blank was moved and the total cost of the expanded path
            if node.action:
                print(f"Action taken: {node.action}")
                print(f"Total cost: {node.cost}.")
                print("")
        # Print additional information
        print("Goal reached!")
        print("Maximum queue size:", frontier_size)
        print("Number of nodes expanded:", nodes_expanded)
        end_cpu_time = time.process_time()
        cpu_time_used = end_cpu_time - start_cpu_time
        print(f"CPU time used: {cpu_time_used} seconds")
    
    # A* Misplaced Tile Trace
    if algorithm_choice == 2:
        if solution_node:
            # Print the trace for A* with Misplaced Tile heuristic
            print("Expanding state")
            print_state(initial_state)  # Print initial state
            print("The best state to expand with g(n) = 0 and h(n) =", solution_node[0].heuristic)  # Print initial heuristic cost
            print("Expanding this node...\n")

            # Print subsequent states and actions along the solution path
            for i, node in enumerate(solution_node[1:], start=1):
                print("The best state to expand with g(n) =", node.cost, "and h(n) =", node.heuristic)  # Print cost and heuristic value
                print("Expanding this node...\n")
                print_state(node.state)  # Print state
                print("Action taken:", node.action)  # Print action taken
                print("")  # Add a blank line for readability

            print("Goal reached!")
            print("Maximum queue size:", frontier_size)
            print("Number of nodes expanded:", nodes_expanded)
            end_cpu_time = time.process_time()
            cpu_time_used = end_cpu_time - start_cpu_time
            print(f"CPU time used: {cpu_time_used} seconds")
        else:
            print("No solution found.")

else:
    print(f"Max queue size: {frontier_size}")
    print("Number of nodes expanded:", nodes_expanded)
    print("No solution found.")
