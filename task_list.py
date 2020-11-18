tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


#Print a list of uncompleted tasks

def uncompleted_tasks(list):
    tasks_to_do = []
    for task in list:
        if task['completed'] == False:
            tasks_to_do.append(task['description'])
    return tasks_to_do       
            
print(uncompleted_tasks(tasks))



# Print a list of completed tasks

def completed_tasks(list):
    tasks_to_do = []
    for task in list:
        if task['completed'] == True:
            tasks_to_do.append(task['description'])
    return tasks_to_do  

print(completed_tasks(tasks))


#Print a list of all task descriptions

def task_description(list):
    for task in list:
        print(task["description"])

task_description(tasks)

# Get tasks where time_taken is at least a given time

def long_tasks(list):
    tasks_to_do = []
    for task in list:
        if task['time_taken'] > 20:
            tasks_to_do.append(task['description'])
    return tasks_to_do   

print(long_tasks(tasks))

# Question 5
# def task_details(list, task_description):
#     information_about_task = None
#     for task in list:
#         if task_description == list["description"]:
#             #return task
#             information_about_task = task
#     return information_about_task        

# print(task_details(tasks, "Wash Dishes"))


