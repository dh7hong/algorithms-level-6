def solution(n, info):
    best_diff = 0
    best_distribution = [-1]

    def dfs(index, arrows_left, ryan_distribution):
        nonlocal best_diff, best_distribution

        # Base case: All points checked or no arrows left
        if index == 11 or arrows_left == 0:
            # Assign remaining arrows to lowest point (0 points)
            if arrows_left > 0:
                ryan_distribution[10] += arrows_left

            ryan_score, apeach_score = 0, 0
            for i in range(11):
                if info[i] == 0 and ryan_distribution[i] == 0:
                    continue
                if ryan_distribution[i] > info[i]:
                    ryan_score += 10 - i
                else:
                    apeach_score += 10 - i

            # Check if Ryan wins with better score difference
            if ryan_score > apeach_score:
                diff = ryan_score - apeach_score
                if diff > best_diff or (diff == best_diff and is_better(ryan_distribution, best_distribution)):
                    best_diff = diff
                    best_distribution = ryan_distribution[:]

            # Backtrack extra arrows assigned at end
            if arrows_left > 0:
                ryan_distribution[10] -= arrows_left

            return

        # Option 1: Ryan tries to win this point
        required_arrows = info[index] + 1
        if required_arrows <= arrows_left:
            ryan_distribution[index] = required_arrows
            dfs(index + 1, arrows_left - required_arrows, ryan_distribution)
            ryan_distribution[index] = 0  # Backtrack

        # Option 2: Ryan skips this point
        dfs(index + 1, arrows_left, ryan_distribution)

    def is_better(dist1, dist2):
        # Tie-breaking condition: More arrows on lower points is better
        for i in range(10, -1, -1):
            if dist1[i] > dist2[i]:
                return True
            elif dist1[i] < dist2[i]:
                return False
        return False  # Equal distributions

    dfs(0, n, [0]*11)
    return best_distribution

# Test examples
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # Expected: [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # Expected: [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))  # Expected: [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3])) # Expected: [1,1,1,1,1,1,1,1,0,0,2]
