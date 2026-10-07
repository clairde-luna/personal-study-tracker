import json

# an empty list for our tasks
tasks = []

# defines the function where the user accesses the menu
def show_menu():
  print("\n=== PERSONAL STUDY TRACKER ===")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Mark a task complete")
  print("4. View progress")
  print("5. Exit")

#function that lets us add a task
def add_task():
  name = input("Enter task name: ")
  subject = input("Enter subject: ")
  task = {
    "name": name,
    "subject": subject,
    "completed": False
  }
  
  tasks.append(task)
  save_tasks()
  print("Task added successfully!")

#  function that displays all your tasks
def view_tasks():
  
  # checks if the list is empty or not
  if not tasks:
    print("No tasks yet!")
    # exit the function early
    return
    
  for task in tasks:
    if task["completed"]:
      status = "Completed"
    else:
      status = "Incomplete"

    # this prints: "Task Name (Subject) - Completion Status"
    print(f"{task['name']}({task['subject']}) - {status}")

# function used to complete a task
def complete_task():
  if not tasks:
    print("No tasks to complete!")
    return
    
  view_tasks()
  choice = input("Which task would you like to complete? ")
  
  index = int(choice) - 1
  task = tasks[index]
  
  task["completed"] = True
  
  save_tasks()
  print("Task marked as complete!")

# saving tasks
def save_tasks():
  # this basically opens the file for writing, "w" means write; then we get a temporary connection to the file.
  with open("tasks.json", "w") as file:
    # this takes the python tasks list and write it into the file tasks.json as JSON
    json.dump(tasks, file)

# loading tasks
def load_tasks():
  # r means read
  with open("tasks.json", "r") as file:
    # this basically asks for the python data of json
    return json.load(file)

# seeing the completion progress!
def view_progress():

  total_tasks = len(tasks)
  if total_tasks == 0:
    print("No tasks yet!")
    return

  completed_tasks = 0
  
  for task in tasks:
    if task["completed"]:
      completed_tasks += 1
      
  # remaining amount of tasks
  incomplete_tasks = total_tasks - completed_tasks
  
  # finding percentage for completion rate!
  completion_rate = (completed_tasks / total_tasks) * 100

# main logic
def main():
  global tasks
  tasks = load_tasks()
  
  print("\n=== YOUR STUDY TRACKER ====")
  while True:
    show_menu()

    # declare a string variable for choice:
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("\n=== YOUR PROGRESS ===")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed: {completed_tasks}")
        print(f"Incomplete: {incomplete_tasks}")
        print(f"Completion rate: {completion_rate}%")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
      print("Invalid choice. Please try again.")

# only run main() when you're executing the file
if __name__ == "__main__":
  main()
