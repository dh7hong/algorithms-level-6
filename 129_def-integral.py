def solution(k, ranges):
    # Generate the Collatz sequence
    sequence = [k]  # List to store the sequence values
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
        sequence.append(k)  # Store the new number
    
    n = len(sequence) - 1  # Total number of steps in the sequence

    # Compute the area under the curve using the trapezoidal rule
    areas = []
    for i in range(n):  
        # Trapezoidal area between sequence[i] and sequence[i+1]
        area = (sequence[i] + sequence[i + 1]) / 2  
        areas.append(area)  # Store computed areas for each interval

    results = []
    for a, b in ranges:
        end = n + b  # Convert `b` to absolute index
        
        # If the range is invalid, return -1.0
        if a > end:
            results.append(-1.0)
        else:
            # Sum the areas in the given range [a, end]
            integral_value = sum(areas[a:end])
            results.append(float(integral_value))  # Convert to float
    
    return results

# Example test cases
print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))  # Expected: [33.0, 31.5, 0.0, -1.0]
print(solution(3, [[0,0], [1,-2], [3,-3]]))       # Expected: [47.0, 36.0, 12.0]
