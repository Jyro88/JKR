class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic


    def path(self):
        node, path_back = self, []

        # Traverse the path from the current node back to the root (initial state)
        while node:
            # Append the current node to the list
            path_back.append(node)
            # Move to the parent node (moves one step closer to the root)
            node = node.parent

        # Reverse the list to get the path from initial state to current state
        path_back_reversed = list(reversed(path_back))
        return path_back_reversed

    def __lt__(self, other):
        return self.cost < other.cost
