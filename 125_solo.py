def solution(cards):
    n = len(cards)  # Total number of boxes
    visited = [False] * n  # Track visited boxes
    group_sizes = []  # Store sizes of all discovered groups

    # Function to traverse a cycle (group)
    def traverse_group(start):
        count = 0
        current = start
        while not visited[current]:  # Continue until a visited box is encountered
            visited[current] = True  # Mark box as visited
            count += 1
            current = cards[current] - 1  # Move to the box indicated by the number
        return count

    # Identify all groups in the permutation
    for i in range(n):
        if not visited[i]:  # Start a new group if the box hasn't been visited
            group_sizes.append(traverse_group(i))

    # If only one group exists, score is 0 (no valid second group)
    if len(group_sizes) < 2:
        return 0

    # Sort group sizes in descending order
    group_sizes.sort(reverse=True)

    # Multiply the sizes of the two largest groups for the final score
    return group_sizes[0] * group_sizes[1]

# Test case
print(solution([8,6,3,7,2,5,1,4]))  # Output: 12


def solution2(cards):
    n = len(cards)
    total_score = 0

    for i in range(n):  # First pick
        visited = [0] * n
        visited[i] = 1
        cur = cards[i] - 1

        while visited[cur] == 0:
            visited[cur] = 1
            cur = cards[cur] - 1

        score_1 = visited.count(1)
        second_list = [x for x in range(n) if visited[x] == 0]  # List of unvisited indices

        score_2 = 0
        if score_1 < n:  # Ensure there is a valid second pick
            for j in second_list:
                visited_2 = visited.copy()  # Correctly create a copy of visited
                visited_2[j] = 1
                curr = cards[j] - 1

                while visited_2[curr] == 0:
                    visited_2[curr] = 1
                    curr = cards[curr] - 1

                score_2 = max(visited_2.count(1) - visited.count(1), score_2)

        total_score = max(score_1 * score_2, total_score)

    return total_score

# Test Case
cards = [8, 6, 3, 7, 2, 5, 1, 4]
print(solution2(cards))  # Expected output: 12
