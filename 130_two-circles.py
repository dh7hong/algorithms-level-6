import math

def solution(r1, r2):
    count = 0

    for x in range(1, r2 + 1):  # Iterate from x = 1 to r2 (avoid double-counting x=0 case)
        y_max = math.floor(math.sqrt(r2**2 - x**2))  # Largest y inside the outer circle
        y_min = math.ceil(math.sqrt(r1**2 - x**2)) if r1**2 - x**2 >= 0 else 1  # Smallest y inside the inner circle

        count += (y_max - y_min + 1)  # Count valid integer y values for this x

    # Multiply by 4 for all quadrants + separately count points on x-axis (x=0)
    axis_count = math.floor(math.sqrt(r2**2)) - math.ceil(math.sqrt(r1**2))
    return count * 4 + axis_count * 4  # Multiply by 4 for quadrants, add y-axis separately

# Test case
print(solution(2, 3))  # Expected output: 20
