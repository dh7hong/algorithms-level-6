def solution(n, l, r):
    def is_one_iterative(idx):
        # Iteratively determine if a position is '1' or '0'
        while idx > 1:
            parent, pos = divmod(idx - 1, 5)
            # Middle position is always zero (3rd position, pos == 2)
            if pos == 2:
                return 0
            # Move up to the parent position
            idx = parent + 1
        # Base position is always '1'
        return 1

    count = 0
    for idx in range(l, r + 1):
        count += is_one_iterative(idx)

    return count

# Test case provided
print(solution(2, 4, 17))  # Output: 8
