from collections import deque

def bfs(start, target, maps):
    """ Performs BFS to find the shortest path between two points in the maze """
    rows, cols = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set([start])

    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == target:  # If we reach the target
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if maps[nr][nc] != 'X':  # Only move if it's not a wall
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))

    return -1  # If no path exists

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    
    # Locate S, L, and E
    start = lever = exit = None
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    # Find shortest paths
    to_lever = bfs(start, lever, maps)
    to_exit = bfs(lever, exit, maps)
    
    if to_lever == -1 or to_exit == -1:
        return -1  # If either path doesn't exist, return -1
    
    return to_lever + to_exit  # Total shortest time

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))