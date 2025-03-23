def solution(board):
    # Count how many O's and X's are in the board
    o_count = 0
    x_count = 0

    for row in board:
        for cell in row:
            if cell == 'O':
                o_count += 1
            elif cell == 'X':
                x_count += 1

    # Rule 1: O should always be equal to X or X should be just one less than O
    if not (o_count == x_count or o_count == x_count + 1):
        return 0  # Invalid turn sequence

    # Function to check if a player has won
    def is_winner(player):
        # Check rows
        for i in range(3):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                return True  # Row win
        
        # Check columns
        for j in range(3):
            if board[0][j] == player and board[1][j] == player and board[2][j] == player:
                return True  # Column win
        
        # Check main diagonal
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True  # Main diagonal win
        
        # Check other diagonal
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True  # Other diagonal win

        return False  # No win found

    # Check if someone has won
    o_wins = is_winner('O')
    x_wins = is_winner('X')

    # Rule 2: If X has won, then O should have played exactly as many times as X
    if x_wins and o_count != x_count:
        return 0  # X can't win unless O and X played equally

    # Rule 3: If O has won, then O should have played one more time than X
    if o_wins and o_count != x_count + 1:
        return 0  # O can't win unless it played exactly one more turn

    # If all rules are followed, it's a valid board
    return 1

print(solution(["O.X", ".O.", "..X"]))  # 1 (Valid)
print(solution(["OOO", "...", "XXX"]))  # 0 (Invalid, both can't win)
print(solution(["...", ".X.", "..."]))  # 0 (Invalid, no O to start)
print(solution(["...", "...", "..."]))  # 1 (Valid, empty board)