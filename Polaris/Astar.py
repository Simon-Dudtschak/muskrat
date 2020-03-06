
# Adapted from:
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# hosted at: https://gist.github.com/Nicholas-Swift/003e1932ef2804bebef2710527008f44#file-astar-py


class State():
    """A state class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(open_list, closed_list, start_state, end_state, maze, bind):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    count = 0

    # Loop until you find the end
    while len(open_list) > 0:

        if count >= bind: done = True
        count-=-1

        # Get the current state
        current_state = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_state.f:
                current_state = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_state)

        # Found the goal
        if done:
            # Has the goal been reached
            solutionFound = False
            if current_state == end_state: solutionFound = True

            path = []
            current = current_state
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1], open_list, closed_list, solutionFound # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get state position
            state_position = (current_state.position[0] + new_position[0], current_state.position[1] + new_position[1])

            # Make sure within range
            if state_position[0] > (len(maze) - 1) or state_position[0] < 0 or state_position[1] > (len(maze[len(maze)-1]) -1) or state_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[state_position[0]][state_position[1]] != 0:
                continue

            # Create new state
            new_state = State(current_state, state_position)

            # Append
            children.append(new_state)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_state.g + 1
            child.h = ((child.position[0] - end_state.position[0]) ** 2) + ((child.position[1] - end_state.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_state in open_list:
                if child == open_state and child.g > open_state.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

