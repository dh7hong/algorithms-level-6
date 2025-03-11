def solution(picks, minerals):
    # Fatigue table: [diamond pickaxe, iron pickaxe, stone pickaxe]
    fatigue_table = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }

    # Total number of pickaxes available
    total_picks = sum(picks)

    # Step 1: Divide minerals into groups of 5
    mineral_groups = [minerals[i:i+5] for i in range(0, len(minerals), 5)]

    # **Edge Case Handling**: Limit groups to the number of available pickaxes
    if len(mineral_groups) > total_picks:
        mineral_groups = mineral_groups[:total_picks]  # Only process as many as pickaxes available

    # Step 2: Sort groups based on priority (diamond count first, iron second)
    def group_value(group):
        return (group.count("diamond"), group.count("iron"))

    mineral_groups.sort(key=group_value, reverse=True)

    total_fatigue = 0  # Track the fatigue cost

    # Step 3: Assign pickaxes optimally
    for group in mineral_groups:
        if picks[0] > 0:   # Use Diamond pickaxe first
            pickaxe_type = 0
            picks[0] -= 1
        elif picks[1] > 0: # Then Iron pickaxe
            pickaxe_type = 1
            picks[1] -= 1
        elif picks[2] > 0: # Then Stone pickaxe
            pickaxe_type = 2
            picks[2] -= 1
        else:
            break  # No more pickaxes available

        # Calculate fatigue for the group
        for mineral in group:
            total_fatigue += fatigue_table[mineral][pickaxe_type]

    return total_fatigue

# **Test Cases including Edge Cases**
test_cases = [
    ([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]),  # Expected 12
    ([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]),  # Expected 50
    ([2, 1, 0], ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]),  # Only diamond, Expected 10
    ([0, 0, 1], ["diamond", "diamond", "diamond", "diamond", "diamond"]),  # Only stone pickaxe, Expected 125
    ([1, 0, 0], ["stone", "stone", "stone", "stone", "stone"]),  # Only stone, but diamond pickaxe available, Expected 5
    ([1, 1, 1], ["iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond"]),  # Mixed, Expected 11
    ([3, 3, 3], ["stone"] * 50),  # All stone, Expected 50
]

# Run tests
results = [solution(picks, minerals) for picks, minerals in test_cases]
results
