from queue import PriorityQueue
# These is the number of nodes
v = 14
# Creating the graph which has list of list
# graph=[

#     []
#     []
#     []
#     []
# ]
graph = [[] for i in range(v)]
# creating the bfs funciton to calculate the lower cost dist

def best_first_search(actual_search, target, n):
    # These is the list of the false with all index with size n [f|f|f|f|f|]
    vis = [False] * n
    # creating the priority queue foe the storage purpose
    pq = PriorityQueue()
    # putting the source node in the queue
    pq.put((0, actual_search))
    vis[actual_search] = True

    while pq.empty() == False:
        # deleete the minimum
        store = pq.get()[1]
        print(store)
        # if the deleted element is target then stop other wise continue
        if store == target:
            break
        # check for each neighbour of the removed element in the quueue
        for node, cost in graph[store]:
            # check if it is visited or not if not visied then we have to visit the node and then add the node in the prioq
            if vis[node] == False:
                vis[node] = True
                pq.put((cost, node))
# add the edge to the graph with cost


# graph[[[1,3],[0,3]]]
'''
vis": [
false,
false,
false,
false,
false,
false,
false,
false,
false,
false,
false,
false,
false,
false
]
'''
def addedge(x, y, cost):
    # add the cost and node value to x and y to x and cost of the x
    graph[x].append((y, cost))
    graph[y].append((x, cost))


# these is creating the graph by adding the actual edge and cost values
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

src = 0
tar = 9
print("The best first earch with min cot is")
best_first_search(src, tar, v)