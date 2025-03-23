def solution(cap, n, deliveries, pickups):
    total_distance = 0

    # Start from the farthest house
    deliver_idx = n - 1  # last delivery index
    pickup_idx = n - 1   # last pickup index

    # Continue until all deliveries and pickups are done
    while deliver_idx >= 0 or pickup_idx >= 0:
        
        # Find the farthest house still needing deliveries
        while deliver_idx >= 0 and deliveries[deliver_idx] == 0:
            deliver_idx -= 1
        
        # Find the farthest house still needing pickups
        while pickup_idx >= 0 and pickups[pickup_idx] == 0:
            pickup_idx -= 1
        
        # If all tasks are done, break
        if deliver_idx < 0 and pickup_idx < 0:
            break

        # Calculate current round-trip distance (go to the farthest needed house and come back)
        trip_distance = max(deliver_idx, pickup_idx) + 1
        total_distance += trip_distance * 2

        # Load the truck for deliveries
        boxes_to_deliver = cap
        i = deliver_idx
        while i >= 0 and boxes_to_deliver > 0:
            if deliveries[i] <= boxes_to_deliver:
                boxes_to_deliver -= deliveries[i]
                deliveries[i] = 0
                i -= 1
            else:
                deliveries[i] -= boxes_to_deliver
                boxes_to_deliver = 0
        deliver_idx = i  # update deliver_idx after delivery

        # Load the truck for pickups
        boxes_to_pickup = cap
        j = pickup_idx
        while j >= 0 and boxes_to_pickup > 0:
            if pickups[j] <= boxes_to_pickup:
                boxes_to_pickup -= pickups[j]
                pickups[j] = 0
                j -= 1
            else:
                pickups[j] -= boxes_to_pickup
                boxes_to_pickup = 0
        pickup_idx = j  # update pickup_idx after pickup

    return total_distance

# Test the implementation with provided examples:

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))  # Expected output: 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))  # Expected output: 30
