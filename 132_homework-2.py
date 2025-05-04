from collections import deque

def solution(plans):
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m

    plans.sort(key=lambda x: time_to_minutes(x[1]))
    task_queue = deque([(name, time_to_minutes(start), int(playtime)) for name, start, playtime in plans])

    paused_tasks = []  # Stack of paused tasks (LIFO)
    completed_tasks = []  # Tasks completed in order

    current_time = 0

    while task_queue:
        name, start_time, duration = task_queue.popleft()

        # Complete paused tasks if there is available time
        while paused_tasks and current_time < start_time:
            paused_name, paused_duration = paused_tasks.pop()

            if current_time + paused_duration <= start_time:
                current_time += paused_duration
                completed_tasks.append(paused_name)
            else:
                paused_duration -= (start_time - current_time)
                paused_tasks.append((paused_name, paused_duration))
                current_time = start_time
                break

        current_time = max(current_time, start_time)
        task_end_time = current_time + duration

        # Check clearly for the overlap with next task
        if task_queue and task_end_time > task_queue[0][1]:
            overlap = task_end_time - task_queue[0][1]
            paused_tasks.append((name, overlap))
            current_time = task_queue[0][1]  # update explicitly to next task start
        else:
            completed_tasks.append(name)
            current_time = task_end_time

    # Finish all paused tasks
    while paused_tasks:
        completed_tasks.append(paused_tasks.pop()[0])

    return completed_tasks

# Testing corrected logic:
print(solution([
    ["science", "12:40", "50"], 
    ["music", "12:20", "40"], 
    ["history", "14:00", "30"], 
    ["computer", "12:30", "100"]
]))
