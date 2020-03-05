from Astar import astar, Node

def main():
    print("Initializing Nav...")

    """ INITILIAZE VARIABLES"""
    # Rover position
    start = []

    # Goal position
    end = []

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    """ BEGIN PATHFINDING """
    


if __name__ == '__main__':
    main()
