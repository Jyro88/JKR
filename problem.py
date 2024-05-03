class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        actions = []
        blank_index = state.index(0)
        if blank_index - 3 >= 0: # Check if blank is on top row
            actions.append('up')
        if blank_index + 3 < len(state): # Check if blank is on bottom row
            actions.append('down')
        if blank_index % 3 != 0: # Check if blank is in first collumn
            actions.append('left')
        if (blank_index + 1) % 3 != 0: # Check is blank is in last collumn
            actions.append('right')
        return actions

    def result(self, state, action):
        new_state = state[:] # Copy the state to the new state
        blank_index = new_state.index(0)

        # Perform one of the 4 operators based on the action parameter given
        if action == 'up':
            new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
        elif action == 'down':
            new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
        elif action == 'left':
            new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        elif action == 'right':
            new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        return new_state

    def goal_test(self, state):
        return state == self.goal_state

    def step_cost(self, state, action):
        return 1
    
    def heuristic(self, state):
        # Calculate the heuristic cost (number of misplaced tiles)
        misplaced = sum(1 for s, g in zip(state, self.goal_state) if s != g)
        return misplaced
