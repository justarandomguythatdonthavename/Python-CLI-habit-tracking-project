import csv
import datetime

csvFile = "habits.csv"

def loadHabits():
    habits=[]
    try:
        with open(csvFile, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                habits.append({
                    "Habit":row["Habit"],
                    "Streak":int(row["Streak"]),
                    "LastEdited": datetime.datetime.strptime(row["LastEdited"],"%Y-%m-%d")
                })
    except FileNotFoundError:
        print("Nothing is found, Check the code for you file Name.")
        pass
    return habits
            
def SaveHabits(habits):
    with open(csvFile,'w',newline="") as file:
        FieldName = ["Habit","Streak","LastEdited"]
        writer = csv.DictWriter(file, fieldnames =  FieldName)
        writer.writeheader()
        for habit in habits:
            writer.writerow({
                "Habit": habit["Habit"],
                "Streak": habit["Streak"],
                "LastEdited": habit["LastEdited"].strftime("%Y-%m-%d")
            })


def AddHabits(habits):
    habitName = input("Enter your habits: ")
    habits.append({
        "Habit": habitName,
        "Streak": 0,
        "LastEdited": datetime.date.today()
    })

    SaveHabits(habits)
    print(f'Habit {habitName} added.')

def MarkDone(habits):
    print("Select an habit to mark as complete:")
    for i, habit in enumerate(habits):
        print(f"{i+1}: {habit['Habit']}")
    choice = int(input("Enter your number: ")) - 1
    if  0 <= choice < len(habits):
        habits[choice]["Streak"] += 1
        habits[choice]["LastEdited"] = datetime.date.today()
        SaveHabits(habits)
        print(f'Habit {habits[choice]["Habit"]} marked as done.')
    else:
        print("Invalid selection")

def viewHabits(habits):
    print("------------------------------------------------------------------")
    for i, habit in enumerate(habits):
        print(f"| {i+1}. Habit: {habit['Habit']} — {habit['Streak']} days streak, last done {habit['LastEdited']}")
    print("------------------------------------------------------------------")

def main():
    habits = loadHabits()

    while True:
        print("Habit Tracker Menu: ")
        print("1. Add New habit: ")
        print("2. Mark Habits as Done")
        print("3. View Habits")
        print("4. Quit")
        choice = int(input("Enter your selection: "))
        match choice:
            case 1:
                AddHabits(habits)
            case 2:
                MarkDone(habits)
            case 3:
                viewHabits(habits)
            case 4:
                break
            case _:
                print("Invalid input, try again")

main()
