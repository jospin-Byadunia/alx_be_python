task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else: 
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that should be completed soon.")
        else:
            print(f"Note: {task} is a medium priority task. You can schedule it for later.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task, but it should be completed soon.")
        else:
            print(f"Note: {task} is a low priority task. You can schedule it for later.")