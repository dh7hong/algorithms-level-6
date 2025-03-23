import heapq

def solution(n, k, enemy):
    max_heap = []  # Max heap (negative values for max-heap behavior)
    total_soldiers_used = 0  # Track total soldiers used
    
    for round_num, enemies in enumerate(enemy):
        heapq.heappush(max_heap, -enemies)  # Push enemy count as negative (to simulate max heap)
        total_soldiers_used += enemies  # Use soldiers to defend
        
        # If soldiers are not enough, try to use an invincibility shield
        if total_soldiers_used > n:
            if k > 0:  # If we still have shields available
                largest_enemy = -heapq.heappop(max_heap)  
                # Remove the largest enemy wave
                total_soldiers_used -= largest_enemy  
                # Refund those soldiers
                k -= 1  # Decrease invincibility shield count
            else:
                return round_num  # Game over, return the last successful round number
    
    return len(enemy)  # If we survive all rounds, return total rounds
