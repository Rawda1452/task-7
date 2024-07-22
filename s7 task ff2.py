def to_do_list():
    tasks=[]
    while True:
        print("a. Add Task")
        print("b. view Tasks")
        print("c. Mark Task as Done") 
        print("d.delete")
        choice=input("enter your choice: ")
        if choice=="a":
            print()
            n_tasks = int(input("How may task you want to add: "))
            for i in range(n_tasks):
                task = input("Enter the tasks: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
        elif choice=="b":
            print("nTasks:")
            for index , task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")                
        elif choice == "c":
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        elif choice=="d":
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task['task']}' deleted!")
            else:
                print("Invalid task number.")
        else:
            print("Invalid choice")
to_do_list()