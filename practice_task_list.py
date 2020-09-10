tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def get_uncompleted_tasks(tasklist):
    uncompleted_tasks = [ ]
    for task in tasklist:
        if task["completed"] == False:
            uncompleted_tasks.append(task)

    return uncompleted_tasks

# 2. Print a list of completed tasks

# 3. Print a list of all task descriptions

# 4. Print a list of tasks where time_taken is at least a given time

# 5. Print any task with a given description

# def count_eggs( list ):
#     total_eggs = 0

#     for bird in list:
#         total_eggs += bird["eggs"]
#         bird["eggs"] = 0 # eggs have been collected

#     return f"{total_eggs} eggs collected"

# print(count_eggs(chickens))