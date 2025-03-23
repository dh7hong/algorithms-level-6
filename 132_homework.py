from collections import deque

def solution(plans):

    # Converts a time string ("HH:MM") into total minutes from midnight
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m

    # Sort the tasks based on their start times (earliest task first)
    plans.sort(key=lambda x: time_to_minutes(x[1]))

    # Queue of tasks waiting to be started (name, start time, duration)
    task_queue = deque([(name, time_to_minutes(start), int(playtime)) for name, start, playtime in plans])
    paused_tasks = []  # Stack to store tasks that were paused
    completed_tasks = []  # List to keep track of completed tasks

    current_time = 0  # Tracks the current time during task execution

    # Process each task in the task queue
    while task_queue:
        name, start_time, duration = task_queue.popleft()
        print(f'Starting new task: {name}, Start time: {start_time}, Duration: {duration}')

        # If there is available time before the next task, try completing paused tasks
        while paused_tasks and current_time < start_time:
            last_task, remaining_time = paused_tasks.pop()
            print(f'Trying to finish paused task: {last_task}, Remaining time: {remaining_time}, Current time: {current_time}')

            # Check if the paused task can be completed before the new task starts
            if current_time + remaining_time <= start_time:
                current_time += remaining_time
                completed_tasks.append(last_task)
                print(f'Finished paused task: {last_task}, Current time: {current_time}')
            else:
                # Not enough time, so pause it again
                remaining_time -= (start_time - current_time)
                paused_tasks.append((last_task, remaining_time))
                print(f'Paused task again: {last_task}, New remaining time: {remaining_time}')
                current_time = start_time
                break

        # Update current time to reflect working on the new task
        current_time = start_time + duration
        print(f'Working on task: {name}, Updated current time: {current_time}')

        # Check if the task completes immediately or needs to be paused
        if not task_queue or task_queue[0][1] >= current_time:
            completed_tasks.append(name)
            print(f'Task completed immediately: {name}')
        else:
            # Pause task because it overlaps with the next one
            remaining_time = current_time - task_queue[0][1]
            paused_tasks.append((name, remaining_time))
            print(f'Task paused: {name}, Remaining time: {remaining_time}')

    # Finish all paused tasks after processing the main queue
    while paused_tasks:
        last_task = paused_tasks.pop()[0]
        completed_tasks.append(last_task)
        print(f'Finishing paused task at the end: {last_task}')

    return completed_tasks

# Test cases to demonstrate how the code works
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))