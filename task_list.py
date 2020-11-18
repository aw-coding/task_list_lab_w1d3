tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# Question 2
# Print  alist 


# def uncompleted_tasks(list):
#     tasks_to_do = []
#     for task in list:
#         if task['completed'] == False:
#             tasks_to_do.append(task['description'])
#     return tasks_to_do       
            



#print(uncompleted_tasks(tasks))



# # Question 2

# # all_tasks = tasks[("description")]
# # print(all_tasks)

# def uncompleted_tasks(list, condition):
#     tasks_to_do = []
#     for task in list:
#         if task['completed'] == condition:
#             tasks_to_do.append(task['description'])
#     return tasks_to_do  

# print(uncompleted_tasks(tasks, True))


# Question 3

# def create_list_of_task_descriptions(list):
#     tasks_descriptions = []
#     for task in list:
# #        if task['completed'] == condition:
#         tasks_descriptions.append(task["description"])
#     return tasks_descriptions 

# print(create_list_of_task_descriptions(tasks))


# Question 4

# def long_tasks(list):
#     tasks_to_do = []
#     for task in list:
#         if task['time_taken'] > 20:
#             tasks_to_do.append(task['description'])
#     return tasks_to_do   

# print(long_tasks(tasks))

# Question 5
def task_details(list, task_description):
    information_about_task = None
    for task in list:
        if task_description == list["description"]:
            information_about_task = task
    return information_about_task        

print(task_details(tasks, "Wash Dishes"))


