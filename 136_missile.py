def solution(targets):
    # Sort intervals by their end point (ascending)
    targets.sort(key=lambda x: x[1])

    missile_count = 0            
    # Counter for interceptors needed
    interceptor_pos = -1         
    # Current interceptor missile position (initially none)

    for start, end in targets:
        # If current interceptor position is within the interval, 
        # no new interceptor needed
        if interceptor_pos >= start:
            continue
        else:
            # Otherwise, launch a new interceptor just before 'end'
            interceptor_pos = end - 0.1  
            # Using end - small epsilon to represent open interval
            missile_count += 1

    return missile_count

# Example Test
print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))  # Expected output: 3
