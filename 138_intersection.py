def solution(line):
    points = set()  # to store unique intersection points (x, y)
    
    # Step 1: Compute all intersections
    for i in range(len(line)):
        A1, B1, C1 = line[i]
        for j in range(i+1, len(line)):
            A2, B2, C2 = line[j]
            denominator = A1 * B2 - A2 * B1
            
            # Skip parallel lines (no intersection)
            if denominator == 0:
                continue
                
            # Intersection using Cramer's rule
            x_numerator = B1 * C2 - B2 * C1
            y_numerator = C1 * A2 - C2 * A1

            # Check if intersection is at integer coordinates
            if x_numerator % denominator == 0 and y_numerator % denominator == 0:
                x = x_numerator // denominator
                y = y_numerator // denominator
                points.add((x, y))
    
    # Step 2: Find minimum bounding rectangle coordinates
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    # Step 3: Create the grid initialized with dots
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # Step 4: Mark the stars (intersections)
    for x, y in points:
        # Translate coordinate system to grid indexing
        grid_y = max_y - y  # Flip y to match grid indexing (top-down)
        grid_x = x - min_x
        grid[grid_y][grid_x] = '*'
    
    # Step 5: Convert grid rows into strings
    answer = [''.join(row) for row in grid]
    
    return answer

# Test the provided example:
lines = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

result = solution(lines)
for row in result:
    print(row)
