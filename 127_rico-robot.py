from collections import deque

def solution(board):
    # Get board dimensions
    rows, cols = len(board), len(board[0])
    
    # Directions for movement (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Find the positions of 'R' (robot) and 'G' (goal)
    start, goal = None, None
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start = (r, c)
            elif board[r][c] == 'G':
                goal = (r, c)

    # BFS setup
    queue = deque([(start[0], start[1], 0)])  # (row, col, moves)
    visited = set()
    visited.add(start)

    while queue:
        r, c, moves = queue.popleft()

        # If goal is reached, return number of moves
        if (r, c) == goal:
            return moves

        # Try moving in all four directions
        for dr, dc in directions:
            nr, nc = r, c
            
            # Move in the direction until hitting a wall or obstacle
            while 0 <= nr + dr < rows and 0 <= nc + dc < cols and board[nr + dr][nc + dc] != 'D':
                nr += dr
                nc += dc
            
            # If this position is already visited, skip
            if (nr, nc) in visited:
                continue

            # Mark new position as visited and add to queue
            visited.add((nr, nc))
            queue.append((nr, nc, moves + 1))

    # If we exhaust the queue without reaching 'G', return -1
    return -1

# Example test cases
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))  # Output: 7
print(solution([".D.R", "....", ".G..", "...D"]))  # Output: -1
