import sys

def shortestDistance(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if grid is None:
        return -1

    tup = findPoints(grid)
    buildings = tup[0]
    zeroPoints = tup[1]
    distances = []
    for point in zeroPoints:
        dist = bfs(grid, point, buildings)
        distances += [dist]
        if dist == -1:
           grid[point[0]][point[1]] = -1

    return select(distances)

def shortestDistanceWalk(grid):

    onePoints = findPointsWalk(grid)

    for point in onePoints:
        bfsWalk(grid, point)

    shortestDistance = sys.maxsize
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < 0 and shortestDistance > (grid[i][j] * -1):
                shortestDistance = (grid[i][j] * -1)

    if shortestDistance == sys.maxsize:
        return -1
    else:
        return shortestDistance

def findPoints(grid):
    buildings = 0
    zeroPoints = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                zeroPoints += [[i,j]]
            elif grid[i][j] == 1:
                buildings += 1
    return (buildings, zeroPoints)

def findPointsWalk(grid):
    onePoints = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                onePoints += [[i,j]]
    return onePoints

def bfs(grid, root, targets):
    hits, sumDist = 0, 0
    targetsFound = set()

    while hits < targets:
        q = []
        q.append((root, 0))
        found = False
        visited = set()
        while(len(q) > 0):
            tup = q.pop(0)
            curr = tup[0]
            dist = tup[1]

            if grid[curr[0]][curr[1]] == 1 and (curr[0], curr[1]) not in targetsFound:
                found = True
                sumDist += dist
                targetsFound.add((curr[0], curr[1]))
                break

            if grid[curr[0]][curr[1]] == 0:
                if (curr[0] - 1) >= 0 and grid[curr[0] -1][curr[1]] != 2 and (curr[0] - 1, curr[1]) not in visited:
                    q.append(([curr[0] - 1, curr[1]], dist + 1))
                    visited.add((curr[0] - 1, curr[1]))
                if (curr[0] + 1) < len(grid) and grid[curr[0] + 1][curr[1]] != 2 and (curr[0] + 1, curr[1]) not in visited:
                    q.append(([curr[0] + 1, curr[1]], dist + 1))
                    visited.add((curr[0] + 1, curr[1]))
                if (curr[1] - 1) >= 0 and grid[curr[0]][curr[1] - 1] != 2 and (curr[0], curr[1] - 1) not in visited:
                    q.append(([curr[0], curr[1] - 1], dist + 1))
                    visited.add((curr[0], curr[1] - 1))
                if (curr[1] + 1) < len(grid[0]) and grid[curr[0]][curr[1] + 1] != 2 and (curr[0], curr[1] + 1) not in visited:
                    q.append(([curr[0], curr[1] + 1], dist +1))
                    visited.add((curr[0], curr[1] + 1))

        if found:
            hits += 1
        else:
            return - 1

    return sumDist

def bfsWalk(grid, root):
    q = []
    q.append((root, 0))
    found = False
    visited = set()
    while(len(q) > 0):
        tup = q.pop(0)
        curr = tup[0]
        dist = tup[1]

        if grid[curr[0]][curr[1]] <= 0:
            grid[curr[0]][curr[1]] += dist

        if (curr[0] - 1) >= 0 and grid[curr[0] -1][curr[1]] <= 0  and (curr[0] - 1, curr[1]) not in visited:
            q.append(([curr[0] - 1, curr[1]], dist - 1))
            visited.add((curr[0] - 1, curr[1]))
        if (curr[0] + 1) < len(grid) and grid[curr[0] + 1][curr[1]] <= 0 and (curr[0] + 1, curr[1]) not in visited:
            q.append(([curr[0] + 1, curr[1]], dist - 1))
            visited.add((curr[0] + 1, curr[1]))
        if (curr[1] - 1) >= 0 and grid[curr[0]][curr[1] - 1] <= 0 and (curr[0], curr[1] - 1) not in visited:
            q.append(([curr[0], curr[1] - 1], dist - 1))
            visited.add((curr[0], curr[1] - 1))
        if (curr[1] + 1) < len(grid[0]) and grid[curr[0]][curr[1] + 1] <= 0 and (curr[0], curr[1] + 1) not in visited:
            q.append(([curr[0], curr[1] + 1], dist - 1))
            visited.add((curr[0], curr[1] + 1))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                grid[i][j] = 3

    return

def select(distances):
    min = sys.maxsize
    for dist in distances:
        if dist < min and dist != -1:
            min = dist

    if min == sys.maxsize:
        return -1
    else:
        return min

def main():
    #grid = [[0,1],[1,0]]
    #grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    #print(shortestDistance(grid))
    #print(shortestDistanceWalk(grid))
    grid = [[0,2,0,0,2,2,2,2,2,2,2,0,0,0,0,2,2,1,0,0,2,0,2,0,2,0,0,2,2,2,0,0,2,0,2,0,2,2,2,0,2],
            [0,0,0,0,0,2,2,0,2,0,0,0,0,0,2,0,0,2,2,0,2,2,2,2,0,0,2,2,0,0,2,2,1,0,0,2,2,0,2,0,0],
            [0,0,0,0,2,2,0,0,0,0,0,0,2,2,0,2,2,0,0,0,2,2,2,2,0,0,0,0,2,2,0,0,0,0,0,2,0,0,2,2,0],
            [2,2,0,2,0,0,2,0,0,0,0,0,2,2,2,0,2,2,2,0,0,0,0,0,0,1,2,2,0,0,0,0,2,0,0,2,0,0,0,0,2],
            [0,0,2,2,0,0,2,1,2,0,0,0,0,2,1,0,2,2,0,2,0,0,0,2,1,0,2,2,0,0,0,2,0,0,0,2,2,0,2,0,0],
            [0,0,2,2,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,2,2,2,2,2,0,2,2,1,2,0,2,0,0,0,2,0,2,2,0],
            [2,0,0,0,2,2,0,0,0,2,1,0,2,0,0,0,0,2,0,2,0,2,2,2,0,2,2,2,0,0,0,0,0,0,2,0,0,0,0,0,2],
            [1,0,2,2,0,0,2,0,0,0,2,0,0,0,2,2,2,2,0,0,0,0,2,0,0,2,0,2,1,2,2,0,0,2,0,0,0,0,0,0,0],
            [0,2,0,0,0,1,0,0,2,2,0,0,0,0,2,0,0,2,0,2,2,2,0,0,2,2,0,2,2,2,2,0,0,0,0,2,0,2,0,0,2],
            [0,0,2,2,0,2,2,0,2,0,1,0,0,0,0,0,2,0,0,2,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,2,2,0,0,1],
            [1,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,2,0],
            [0,1,2,2,2,2,0,2,0,0,2,2,0,0,0,0,0,2,0,2,0,0,0,0,2,0,0,0,0,0,0,2,2,2,0,0,2,2,0,0,0],
            [2,0,2,0,2,0,0,2,0,0,0,2,0,0,2,2,0,0,0,2,0,0,2,2,2,0,2,2,0,2,2,1,2,0,0,2,0,0,0,2,0],
            [0,0,2,0,0,0,2,2,2,0,2,2,2,0,0,2,0,0,0,2,1,2,2,0,2,0,2,0,0,2,2,0,0,0,2,2,0,0,0,0,0],
            [0,0,0,0,0,2,2,0,2,0,0,2,0,2,0,0,0,2,0,0,0,0,0,0,0,1,2,0,0,0,0,1,0,2,0,0,2,0,1,0,0],
            [1,2,0,2,0,0,0,2,0,2,0,0,0,0,0,2,1,2,0,0,0,0,0,2,0,0,0,0,0,2,2,0,0,0,2,0,0,1,0,2,2],
            [1,0,0,2,0,2,0,2,0,2,0,0,0,0,1,0,0,0,0,0,2,2,0,2,0,2,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,1,2,2,0,0,2,2,0,0,0,0,0,0,2,0,2,0,2,2,0,1],
            [2,0,0,1,1,0,1,0,2,0,0,2,1,0,2,0,0,2,2,0,2,0,2,2,0,1,2,0,2,0,0,0,0,0,0,2,0,0,2,0,0],
            [2,2,0,0,0,2,2,0,2,2,0,0,0,2,0,0,0,2,0,0,2,0,0,2,0,0,0,2,0,0,0,2,2,2,0,2,0,0,2,0,2]]
    print(shortestDistance(grid))
    #print(shortestDistanceWalk(grid))


if __name__ == '__main__':
    main()
