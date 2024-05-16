"""
Optimal Task Assignment:
There are n workers and m Tasks to be completed.
T is list of positive integers indicating no of hours required for each task.
Every worker can do two tasks and tasks will be done in parallel.
Total time of work is maximum of the sum of pair of tasks done workers.
There are 5 Workers and 10 Tasks and t=[2,3,3,4,5,8,2,1,3,4] find out optimal assignment.

"""


def optimal_task_assignment(tasks):
    # Sort the tasks in ascending order
    sorted_tasks = sorted(tasks)

    # Number of workers
    num_workers = len(tasks) // 2

    # Initialize the list to store the pairs of tasks for each worker
    task_pairs = []

    # Pair tasks by assigning the smallest with the largest, second smallest with the second largest, etc.
    for i in range(num_workers):
        task_pairs.append((sorted_tasks[i], sorted_tasks[-(i + 1)]))

    # Calculate the maximum sum of the pairs
    max_time = max(sum(pair) for pair in task_pairs)

    return task_pairs, max_time


# List of tasks
tasks = [2, 3, 3, 4, 5, 8, 2, 1, 3, 4]

# Get the optimal task assignment and the maximum time
task_pairs, max_time = optimal_task_assignment(tasks)

# Print the results
print("Optimal Task Pairs:")
for i, pair in enumerate(task_pairs):
    print(f"Worker {i + 1}: Task {pair[0]} hours and Task {pair[1]} hours")

print(f"\nOptimal Total Time: {max_time} hours")
