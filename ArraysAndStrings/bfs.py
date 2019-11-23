from collections import deque

"""
Find the minimum distance required to move the robot (9) from the field.

Idea: BFS

"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class QueueNode:
    def __init__(self, pt, distance):
        self.point = pt
        self.dist = distance


def isValid(grid, row, col):
    ROW = len(grid)
    COL = len(grid[0])
    return (row >= 0 and row < ROW) and col >= 0 and col < COL


rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


def find_robot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 9:
                return Point(i, j)


def bfs(matrix, src, dest):
    ROW = len(grid)
    COL = len(grid[0])
    if matrix[src.x][src.y] == 0 or matrix[dest.x][dest.y] == 0:
        return -1

    visited = [[False for i in range(ROW)] for j in range(COL)]
    visited[src.x][src.y] = True
    q = deque()
    s = QueueNode(src, 0)
    q.append(s)
    while q:
        current = q[0]
        pt = current.point
        if pt.x == dest.x and pt.y == dest.y:
            return current.dist
        q.popleft()
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            if isValid(grid, row, col) and matrix[row][col] \
            and not visited[row][col]:
                visited[row][col] = True
                adjCell = QueueNode(Point(row, col), current.dist + 1)
                q.append(adjCell)
    return -1


"""
grid = [[1,1,1,9,0],
        [1,0,0,1,0],
        [1,1,1,1,0],
        [1,1,1,1,0],
        [0,0,0,0,0]]
"""
grid = [[9]]
destination = find_robot(grid)
source = Point(0, 0)
print(bfs(grid, source, destination))
