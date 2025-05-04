def solution(n):
    def is_safe(row, col, queens):
        """Check if a queen can be placed at (row, col)"""
        for r, c in enumerate(queens[:row]):
            if c == col or abs(row - r) == abs(col - c):  
                print(f'Conflict detected: cannot place queen at row={row}, col={col} due to queen at row={r}, col={c}')
                return False
        print(f'Safe placement found at row={row}, col={col}')
        return True

    def backtrack(row, queens):
        """Try to place queens row by row"""
        if row == n:  
            print(f'Valid solution found: {queens}')
            return 1  
        
        count = 0
        for col in range(n):  
            print(f'Attempting placement at row={row}, col={col}, current queens={queens}')
            if is_safe(row, col, queens):
                count += backtrack(row + 1, queens + [col])
            else:
                print(f'Backtracking from row={row}, col={col}')
        return count

    print(f'Starting search for N-Queens solutions, board size = {n}')
    total_solutions = backtrack(0, [])  
    print(f'Total number of solutions: {total_solutions}')
    return total_solutions

# Test case
print(f'Result: {solution(4)}')  # Expected output: 2