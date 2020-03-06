from Astar import astar, State

def main():
    print("Initializing Nav...")

    """ INITILIAZE VARIABLES """

    solutionFound = False
    solutionFoundandTraced = False
    doneTrace = True
    loc = []                        # Rover position
    end = []                        # Goal position
    bind = 10                       # How long to loop astar


    # Turn locations into states
    loc_state = State(None, loc)
    loc_state.g = loc_state.h = loc_state.f = 0
    end_state = State(None, end)
    end_state.g = end_state.h = end_state.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start state
    open_list.append(loc_state)

    """ BEGIN PATHFINDING """

    while loc_state != end_state:
        # Update variables
        loc_state = State(None, loc)
        gmap = [] # Get gmap from ros

        if not solutionFound:
            path, open_list, closed_list, solutionFound = astar(
                                                                open_list, 
                                                                closed_list, 
                                                                loc_state, 
                                                                end_state, 
                                                                gmap, 
                                                                bind
                                                                )
        
        # Move agent along path


if __name__ == '__main__':
    main()
