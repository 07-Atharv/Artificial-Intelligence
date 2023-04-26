
# impelement Depth limit search using recusrion
create_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}


def depth_limit_search(start_node, goal_node, path, level, max_level):
    print("current level", level)
    print("goal node", start_node)
    # we have to add the start node to the graph
    path.append(start_node)
    # check if the goal node is only start node or not
    if(start_node == goal_node):
        return path
    # if the node is not found means we have reached till end level then not found
    if(level == max_level):
        print("Success")
        return False
    # now check the child of the current node
    for store in create_graph[start_node]:
        #if return true or false
        if depth_limit_search(store, goal_node, path,  level+1, max_level):
            return path
        path.pop()
    return False
    # if we do not find the goal node in the child then just ret the false


start_node = 'A'
goal_node = input('Enter the goal or destination node :')
max_level = int(input('Enter the max depth limit of the level'))
path = list()
result_of_dls = depth_limit_search(start_node, goal_node, path, 0, max_level)
if(result_of_dls):
    print("The avaliable path is ")
    print(path)
else:
    print('No path available path for these node')