from Astar import astar, State

def main():
    print("Initializing Nav...")

    """ INITILIAZE VARIABLES"""
    # Rover position
    start = []

    # Goal position
    end = []

    # Create start and end state
    start_state = State(None, start)
    start_state.g = start_state.h = start_state.f = 0
    end_state = State(None, end)
    end_state.g = end_state.h = end_state.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start state
    open_list.append(start_state)

    """ BEGIN PATHFINDING """



if __name__ == '__main__':
    main()
