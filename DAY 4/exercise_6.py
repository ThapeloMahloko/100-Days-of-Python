"""
To-Do List Randomiser 
Write a program that lets the user input a list of task
(e.g., "Do homework", "Clean the room"). Then, randomly shuffle
the tasks and print them in a random order.
"""
# Import Random Module 
import random

# Get tasks from the user 
task_1 = input("Enter your first task: ")
task_2 = input("Enter your second task: ")
task_3 = input("Enter last task: ")

# Make a list of the tasks
tasks = []
tasks.append(task_1)
tasks.append(task_2)
tasks.append(task_3)

# Shuffle the tasks
random.shuffle(tasks)

# Display the task to do
print(tasks[0])