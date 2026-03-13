def print_missions(missions):
    print("Your missions:")
    for i, m in enumerate(missions, 1):
        print(i, "-", m)
    print("--------------------------")
def save_missions(missions):
    with open("missions.txt", "w") as file:
        for mission in missions:
            file.write(mission + "\n")


def load_missions():
    missions = []
    try:
        with open("missions.txt", "r") as file:
            for line in file:
                missions.append(line.strip())
    except FileNotFoundError:
        pass
    return missions
missions = load_missions()

while True:
    print("\n1. Add a mission")
    print("2. Show missions")
    print("3. Delete a mission")
    print("4. Edit a mission")
    print("5. Exit")
    print("--------------------------")

    # اختيار المستخدم مع منع التوقف
    try:
        num = int(input("Choose a number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # --------------------- إضافة مهمة ---------------------
    if num == 1:
        while True:
            user_input = input("Write the mission (or 0 to go back): ")
            if user_input == "0":
                break
            missions.append(user_input)
            print("Mission added successfully!")
            print_missions(missions)
            save_missions(missions)
            break

    # --------------------- عرض المهام ---------------------
    elif num == 2:
        while True:
            if len(missions) == 0:
                print("No missions available.")
                break
            print_missions(missions)
            input("Press Enter to return to main menu...")  # فقط للرجوع بعد العرض

            break

    # --------------------- حذف مهمة ---------------------
    elif num == 3:
        while True:
            if len(missions) == 0:
                print("No missions available to delete.")
                break

            user_input = input("Enter the number of the mission to delete (or 0 to go back): ")
            if user_input == "0":
                break

            try:
                number = int(user_input)
            except ValueError:
                print("Please enter a valid number!")
                continue

            if number < 1 or number > len(missions):
                print(f"Invalid number! Enter a number between 1 and {len(missions)}")
                continue

            missions.pop(number - 1)
            print("Mission deleted successfully!")
            print_missions(missions)
            save_missions(missions)
            break


    # --------------------- تعديل مهمة ---------------------
    elif num == 4:
        while True:
            if len(missions) == 0:
                print("No missions available to edit.")
                break

            user_input = input("Enter the number of the mission to edit (or 0 to go back): ")
            if user_input == "0":
                break

            try:
                number = int(user_input)
            except ValueError:
                print("Please enter a valid number!")
                continue

            if number < 1 or number > len(missions):
                print(f"Invalid number! Enter a number between 1 and {len(missions)}")
                continue

            new_mission = input("Write the new mission: ")
            missions[number - 1] = new_mission
            print("Mission edited successfully!")
            print_missions(missions)
            save_missions(missions)
            break



    # --------------------- إنهاء البرنامج ---------------------
    elif num == 5:
	    option = input("Are you sure you want to exit? (y/n): ")
	    if option.lower() == "y":
		    print("Thank you, you're logged out.")
		    break
	    elif option.lower() == "n":
		    continue
	    else:
		    print("Invalid option, returning to main menu.")
		    continue


    # --------------------- خيار غير صحيح ---------------------
    else:
        print("Please choose a valid option from 1 to 5.")


