def hanoi(n, start, end, auxiliary, moves):
    if n == 1:
        moves.append([start, end])  # Move the only disk from start to end
    else:
        hanoi(n - 1, start, auxiliary, end, moves)  # Move n-1 disks to auxiliary rod
        moves.append([start, end])  # Move the nth (largest) disk to the target rod
        hanoi(n - 1, auxiliary, end, start, moves)  # Move n-1 disks to the target rod

def solution(n):
    moves = []
    hanoi(n, 1, 3, 2, moves)
    return moves

# Example usage
print(solution(2))  # Expected output: [[1, 2], [1, 3], [2, 3]]