"""


Algorithm

Step 1 = Make a open list for the (The open contains the nodes that have not visited, but their neighbors are yet to be explored.)

Step 2  = Make a closed empty list  ( On the other hand, close contains nodes that, along with their neighbors, have been visited)

Step 3 = If it does not reach the destination node then consider the node with the lowest f score in the open list (successor == goal node check )(find the node with lowest g value on the open list )

Step 4 = Put the current node in the list and check its neighbours (now check the nei for the curr node)

Step 5 = For each neighbour of the current node 

Step 6 = If the neigbour has lower g value than the current node and is in the closed list then replace the neighbur with this new node as neighbour parent 

Step 7 =If the current g is lower and neighbour is in the open list replace the nei with lower g value and change the neigh parent to the curr node 

Step 8 = If the nei is not in both the list add it to open list and set its g


"""


class Graph:
    adjecancy_list = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }

    # to take the graph as list

    def __init__(self, adjecancy_list):
        self.adjecancy_list = adjecancy_list

    # to explore the neighbours of the nodes
    def exp_neigh(self, v):
        return self.adjecancy_list[v]

    # These is the heuristic function with all the heuristic values

    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # The open list is for whose nodes have been visited but whose neighbours have been not visited starts of with start node
        # closed list is list of node which have been visited and and whose neighbours have been inspected

        open_list = set([start_node])
        close_list = set([])

        #  g contains the current distance from start_node to all other node the def value if it is not found is infinity
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            # find the node with lowest value of the f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print("Path does not exist")
                return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                rec_path = []

                while parents[n] != n:
                    rec_path.append(n)
                    n = parents[n]
                rec_path.append(start_node)
                rec_path.reverse()

                print("Path found : {}".format(rec_path))
                return rec_path

            # for all neighbors of the current node do
            for (m, weight) in self.exp_neigh(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in close_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n]+weight
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list

                else:
                    if g[m] > g[n]+weight:
                        g[m] = g[n]+weight
                        parents[m] = n
                    if m in close_list:
                        close_list.remove(m)
                        open_list.add(m)

            open_list.remove(n)
            close_list.add(n)

        print("Path does not exist")
        return None


adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')
