# # define the functions 1 init 2 generate child -> find shuffle


# class Node:
#     def __init__(self, datapuz, level, fvalue):
#         self.datapuz = datapuz
#         self.level = level
#         self.fvalue = fvalue

#     def generatechild(self):
#         x, y = self.find(self, self.datapuz, '_')

#         left = [x, y-1]
#         right = [x, y
#
# +1]
#         up = [x-1, y]
#         down = [x+1, y]

#         store_pos = [left, right, up, down]
#         store_child = list()

#         for i in store_pos:
#             genchild = self.shuffle(self, self.datapuz, x, y, i[0], i[1])
#             if genchild is not None:
#                 child = Node(genchild, self.level+1, 0)
#                 store_child.append(genchild)
#                 return child
#             else:
#                 return None

#     def find(self, datap, blank):
#         for i in range(0, 3):
#             for j in range(0, 3):
#                 if datap[i][j] == blank:
#                     return i, j

#     def shuffle(self, datapuz, x1, y1, x2, y2):
#         if x2 >= 0 and x2 < 3 and y2 >= 0 and y2 < 3:
#             store_copy = []
#             store_copy = datapuz
#             temp = store_copy[x2][y2]
#             store_copy[x2][y2] = store_copy[x1][y1]
#             store_copy[x1][y1] = temp
#             return store_copy
#         else:
#             return None


# class Puzzle:
#     def __init__(self, size):
#         self.n = size
#         self.open = []
#         self.close = []

#     def accept(self):
#         puz = []
#         for i in range(0, 3):
#             temp = input().split(" ")
#             puz.append(temp)
#         return puz

# ****************************************************************************************************************************************************
"""
class Node:

    def __init__(self, data, level, fvalue):
        self.data = data
        self.level = level
        self.fvalue = fvalue

    def find(self, data, blank):
        for i in range(0, 3):
            for j in range(0, 3):
                if data[i][j] == blank:
                    return i, j

    def shuffle(self, data, x1, y1, x2, y2):
        if x1 >= 0 and x1 < 3 and x2 >= 0 and x2 < 3:
            store_puz = list()
            store_puz = data
            change = store_puz[x2][y2]
            store_puz[x2][y2] = store_puz[x1][y1]
            store_puz[x1][y1] = change
        else:
            return None

    def generatechild(self):
        x, y = self.find(self.data, '_')
        left = [x, y-1]
        right = [x, y+1]
        up = [x-1, y]
        down = [x+1, y]
        store_pos = [left, right, up, down]

        for i in store_pos:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                store_next = Node(child, self.level+1, 0)
                return store_next
            else:
                return None


class Puzzle:
    def __init__(self):
        self.n = 3
        self.open = []
        self.close = []

    def puzzleinp(self):
        inppuz = [1, 2, 3, 8, '_', 4, 7, 6, 5]
        return inppuz

    def goalinp(self):
        goalpuz = [2, 8, 1, '_', 4, 3, 7, 6, 5]
        return goalpuz

    def fvalue(self, start, goal):
        store_diff = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    store_diff = store_diff+1
        return store_diff+start.level
# 2 Node puzzle


class Node:
    def __init__(self, data, lev, fvalue):
        self.data = data
        self.lev = lev
        self.fvalue = fvalue

    def generate_child(self):
        pone, ptwo = self.find(self.data, '_')

    def find(self, data, blankspace):
        for i in range(0, 3):
            for j in range(0, 3):
                if data[i][j] == blankspace:
                    return i, j

    def shuffle(self, data, x1, x2, y1, y2):
        store_puz = self.data
        if x1 >= 0 and x1 < 3 and x2 >= 0 and x2 < 3:
            copypuz = self.data
            temp = copypuz[x2][y2]
            copypuz[x2][y2] = copypuz[x1][y1]
            copypuz[x1][y1] = temp
    *****************************************************************************************************************************************************
    """


class Node:
    # Initializing the Node with the value
    def __init__(self, puzzle, level, fvalue):
        self.puzzle = puzzle
        self.level = level
        self.fvalue = fvalue

    def genchild(self):
        pone, ptwo = self.find(self.data, '_')
        store_val = list()
        store_val = [[pone, ptwo-1], [pone, ptwo+1],
                     [pone-1, ptwo], [pone+1, ptwo]]
        child_neigh = list()
        for x in store_val:
            store_child = self.shuffle(self.data, pone, ptwo, x[0], x[1])
            if store_child is not None:
                child_Node = Node(self.puzzle, self.level+1, 0)
                child_neigh.append(child_Node)
            return child_neigh

    def find(self, data, blankspace):
        for i in range(0, 3):
            for j in range(0, 3):
                if data[i][j] == blankspace:
                    return i, j

    def shuffle(self, data, x1, y1, x2, y2):
        if x2 >= 0 and x2 < 3 and y2 >= 0 and y2 < 3:
            store_temp = list()
            store_temp = self.data
            temp = store_temp[x2][y2]
            store_temp[x2][y2] = store_temp[x1][y1]
            store_temp[x1][y1] = temp
        else:
            return None


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.close = []
        self.open = []

    def puzzleinp(self):
        inppuz = [1, 2, 3, 8, '_', 4, 7, 6, 5]
        return inppuz

    def goalinp(self):
        goalpuz = [2, 8, 1, '_', 4, 3, 7, 6, 5]
        return goalpuz

    def fvalue(self, start, goal):
        temp = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp = temp+1
        return temp+temp

    def startexe(self):
        start = self.puzzleinp()
        goal = self.goalinp()
        start = Node(start, 0, 0)
        start.fval = self.fvalue(start, goal)
        self.open.append(start)
        while True:
            cur = self.open[0]
            for i in cur.puzzle:
                for j in i:
                    print(j, end=" ")
                print("")
            for i in cur.genchild():
                i.fval = self.fvalue(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            self.open.sort(key=lambda x: x.fval, reverse=False)


store = Puzzle(3)
store.startexe()
