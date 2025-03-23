def solution(name):
    # Step 1: Calculate the total number of moves needed to change letters from 'A' to the correct letters
    total_moves = 0
    n = len(name)  # The length of the name
    
    # Step 2: Calculate the vertical moves (up or down) for each letter
    for char in name:
        up_moves = ord(char) - ord('A')  # Moving up from 'A' to the letter
        down_moves = 26 - up_moves  # Moving down from 'A' to the letter by going backward
        total_moves += min(up_moves, down_moves)  # Choose the smaller number of moves

    # Step 3: Find the best way to move left and right to change letters
    min_side_moves = n - 1  # Worst case: Move straight to the right
    
    for i in range(n):
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1  # Skip 'A's to find the next letter we need to change

        # Move forward to 'i' then return back and go to the end
        option1 = i + i + (n - next_index)
        # Move to the end first then return back to 'i'
        option2 = (n - next_index) + (n - next_index) + i

        # Choose the best option
        min_side_moves = min(min_side_moves, option1, option2)

    # Total moves = Letter changes + best cursor movement
    return total_moves + min_side_moves

# Test cases
print(solution("JEROEN"))  # Expected output: 56
print(solution("JAN"))     # Expected output: 23
