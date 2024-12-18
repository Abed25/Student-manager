isRunning = True
studentNames = list()
userOptions = list(("Register students", "Retrive student","Remove a Student","Edit Student Name","Exit"))
retriveOptions = list(("Search a student by names","List of  all students"))

def show_menu():
    print("\n\nStudent manager")
    for i, option in enumerate(userOptions, start=1):
        print(f"{i}. {option}")
    print("\n")


def Searcher():
    searchEL = input("Enter the name of the Student: ").upper()
    if searchEL in studentNames:
        return searchEL
    else:
        return None

def Register():
    numberOfStudents =int(input("Enter number of students: "))
    print(f"Enter names of {numberOfStudents}: ")
    for i in range(numberOfStudents):
        while True:
            name = input(f"{i+1}. Name: ").strip().upper()
            if name:
                studentNames.append(name)
                print(f"******{name} Added successfully ******")
                break
            else:
                print("Name cannot be empty. Please try again.")

def Retrive():
    print(f"WELCOME TO STUDENT RETRIVAL\n1. {retriveOptions[0]}\n2. {retriveOptions[1]}")
    retriveOpt = int(input(": "))
    if(retriveOpt == 1):
        search = Searcher()
        if search:
            print(f"{search} is available")
        else:
            print(f"Not found!!")
    elif retriveOpt == 2:
        if not studentNames:
            print("No record")
        else:
            for i in range(len(studentNames)):
                print(f"{i+1}. {studentNames[i]}")


def  Remove():
    try:
        delStudentName = Searcher()
        if delStudentName:
            feedback = input(f"I you sure you want to delete {delStudentName}?\n (y)- to continue (n)- to skip: ").lower()
            if (feedback == "y"):
                studentNames.remove(delStudentName)
                print(f"*********{delStudentName} Deleted successfully***********\n")
            elif (feedback == 'n'):
                print(f"*********{delStudentName} Still is in the system***********\n")
            else:
                print("Invalid entry please try again")
        else:
            print("Not found!!!")
        
    except NameError:
        print("Unexpected input please try again")

def Edit():
    nameEdit = Searcher()
    if nameEdit:
        index = studentNames.index(nameEdit)
        newEntry= input(f"You are renaming {nameEdit} to : ").upper()
        studentNames[index] = newEntry
        print("*******Changes made effectively*********")
    else:
        print("Not found!!!")
    
while(isRunning):
    try:
        show_menu()
        opt = int(input("Choose: "))
        if opt == 1:
            Register()
        elif opt == 2:
            Retrive()
        elif opt == 3:
            Remove()
        elif opt == 4:
            Edit()
        elif opt == 5:
            isRunning = False
        else:
            print("Inavalid command input!!!")
    except ValueError:
        print("System expects a number\n")
print("........End .......")