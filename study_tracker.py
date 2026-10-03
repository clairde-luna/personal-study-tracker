# an empty list
tasks = []

# defines the function where the user accesses the menu
def show_menu():
  print("\n=== PERSONAL STUDY TRACKER ===")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Mark a task complete")
  print("4. View progress")
  print("5. Exit")

#  function that displays all your tasks
def view_tasks():
  
  # checks if the list is empty or not
  if not tasks:
    print("No tasks yet!")
    # exit the function early
    return
    
  for  task in tasks:
    # print the task name
    # print the subject
    pass
    # placeholder for after code is written

# main logic
def main():
  print("\n=== YOUR STUDY TRACKER ====")
  while True:
    show_menu()

    # declare a string variable for choice:
    choice = input("Choose an option: ")
    if choice == "1":
        print("Task feature coming soon!")
     elif choice == "2":
        print("View tasks feature coming soon!")
     elif choice == "3":
        print("Completion feature coming soon!")
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
