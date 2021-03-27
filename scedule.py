from task import Task

class Schedule:
    def __init__(self):
        self.schedule = []

    # Gets a users class along with the time and adds it to the schedule array
    def AddClass(self):
        print("----Please add a class----")
        print("----Please enter the time in the 24 hour format")
        classRoom = input("Please enter the google meets link for your class: ")
        Time = input("Please enter the time for your class in the 24 hour format: ")
        self.schedule.append(Task(str(classRoom),str(Time)))
