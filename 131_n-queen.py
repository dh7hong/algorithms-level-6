def solution(n):
    def is_safe(row, col, queens):
        """Check if a queen can be placed at (row, col)"""
        for r, c in enumerate(queens[:row]):
            if c == col or abs(row - r) == abs(col - c):  
                # Same column or diagonal check
                return False
        return True

    def backtrack(row, queens):
        """Try to place queens row by row"""
        if row == n:  
        # Base case: all queens placed
            return 1  
            # Found one valid arrangement
        
        count = 0
        for col in range(n):  
        # Try placing queen in all columns
            if is_safe(row, col, queens):
                count += backtrack(row + 1, queens + [col])  
                # Move to next row
        return count

    return backtrack(0, [])  
    # Start placing from row 0

# Test case
print(solution(4))  # Expected output: 2
