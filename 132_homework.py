from collections import deque

def solution(plans):

    # Convert "hh:mm" format to total minutes
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m  # Convert hours to minutes

    # Sort tasks by start time in ascending order
    plans.sort(key=lambda x: time_to_minutes(x[1]))

    # Convert sorted tasks into a queue with (name, start_time, duration)
    task_queue = deque([(name, time_to_minutes(start), int(playtime)) for name, start, playtime in plans])
    paused_tasks = []  # Stack for interrupted tasks
    completed_tasks = []  # List to store completed task order

    # Start the first task
    current_time = 0

    while task_queue:
        name, start_time, duration = task_queue.popleft()

        # If there's a gap before this task starts, resume paused tasks
        while paused_tasks and current_time < start_time:
            last_task, remaining_time = paused_tasks.pop()
            if current_time + remaining_time <= start_time:
                # If the paused task finishes before the next scheduled task
                current_time += remaining_time
                completed_tasks.append(last_task)
            else:
                # If the paused task still has remaining time, push it back
                paused_tasks.append((last_task, remaining_time - (start_time - current_time)))
                current_time = start_time
                break

        # Start the new task
        current_time = start_time + duration

        # If the next task starts after this one finishes, mark it as completed
        if not task_queue or task_queue[0][1] >= current_time:
            completed_tasks.append(name)
        else:
            # Otherwise, pause the current task with remaining time
            remaining_time = (start_time + duration) - task_queue[0][1]
            paused_tasks.append((name, remaining_time))

    # After processing all scheduled tasks, finish paused tasks in LIFO order
    while paused_tasks:
        completed_tasks.append(paused_tasks.pop()[0])

    return completed_tasks

# Test Cases
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# Expected Output: ["korean", "english", "math"]

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# Expected Output: ["science", "history", "computer", "music"]

print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
# Expected Output: ["bbb", "ccc", "aaa"]
