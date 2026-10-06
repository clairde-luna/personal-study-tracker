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

#  function that displays all your tasks
def view_tasks():
  
  # checks if the list is empty or not
  if not tasks:
    print("No tasks yet!")
    # exit the function early
    return
    
  for  task in tasks:
    if task["completed"]:
      status = "Completed"
    else:
      status = "Incomplete"

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
  print("Task marked as complete!")

# main logic
def main():
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
        print("Progress feature coming soon!")
     elif choice == "5":
        print("Goodbye!")
        break
    else:
      print("Invalid choice. Please try again.")

# only run main() when you're executing the file
if __name__ == "__main__":
  main()
