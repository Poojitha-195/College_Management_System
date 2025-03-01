import otp

class person:
    def __init__(self, id_no, name, email):
        self.id_no = id_no
        self.name = name
        self.email = email

class student(person):
    def __init__(self, id_no, name, email, dept):
        super().__init__(id_no, name, email)
        self.dept = dept
        self.marks = {}

class teacher(person):
    def __init__(self, id_no, name, email, subject):
        super().__init__(id_no, name, email)
        self.subject = subject

class college:
    def __init__(self, cid, name, location):
        self.cid = cid
        self.name = name
        self.location = location
        self.students = []
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def display_teachers(self):
        if len(self.teachers)==0:
            print("No Teachers Present")
        else:
            print("\nTeacher Details")
            for x in self.teachers:
                print(f"Id No: {x.id_no}")
                print(f"Name: {x.name}")
                print(f"Email: {x.email}")
                print(f"Subject: {x.subject}\n")

    def display_students(self):
        if len(self.students)==0:
            print("No Students Present")
        else:
            print("\nStudent Details:")
            for x in self.students:
                print(f"Id No: {x.id_no}")
                print(f"Name: {x.name}")
                print(f"Email: {x.email}")
                print(f"Branch: {x.dept}\n")

    def add_marks(self, student_id, subject, marks):
        for student in self.students:
            if student.id_no == student_id:
                student.marks[subject] = marks
                print(f"Marks Added for {student.name} in {subject}\n")
                return
        print("Student Not Found\n")

    def display_results(self, student_id):
        for student in self.students:
            if student.id_no == student_id:
                print(f"\nResults for {student.name}:")
                if not student.marks:
                    print("No marks added yet.\n")
                else:
                    for subject, marks in student.marks.items():
                        print(f"{subject}: {marks}")
                    print(f"Average Marks: {sum(student.marks.values()) / len(student.marks):.2f}")
                return
        print("Student Not Found\n")

    def display_colleges(colleges):
        if not colleges:
            print("No Colleges are registered\n")
        else:
            print("\nCollege Details")
            for i in colleges:
                print(f"College Id: {i.cid}")
                print(f"College Name: {i.name}")
                print(f"College Location: {i.location}\n")

colleges = []

while True:
    print("Choose Your Option:")
    print("1. Create College")
    print("2. Add Teacher")
    print("3. Add Student")
    print("4. Display Teacher Details")
    print("5. Display Student Details")
    print("6. Display College Details")
    print("7. Add Marks")
    print("8. Display Results")
    print("9. Exit")

    option=int(input("Enter your option:"))
    if option == 1:
        clg_id = int(input("Enter College Id: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x=True
                break
        if x == True:
            print()
            print(f"\nCollege with {clg_id} already exists, Try again\n")
            print()
        else:
            clg_name = input("Enter College Name: ")
            clg_location = input("Enter College Location: ")
            clg=college(clg_id,clg_name,clg_location)
            colleges.append(clg)
            print()
            print("\nCollege Created Successfully\n")
            print("------------------------------------------------")

    elif option == 2:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x=True
                break
        if x == True:
            id_no = input("Enter Teacher ID: ")
            name = input("Enter Teacher Name: ")
            email = input("Enter Teacher Email: ")
            subject = input("Enter Teacher Subject: ")
            otp=otp.send_otp(email)
            for i in range (3):
                enter_otp=int(input("Enter your otp:"))
                if enter_otp == otp:
                    clg.add_teacher(teacher(id_no, name, email, subject))
                    print(f"\nTeacher Added Successfully to {clg.name}\n")
                    print("------------------------------------------------")
                    print()
                    break
                else:
                    print("Invalid otp")
                    print()
            print("Try again by sending new otp")
            print()
                    
        else:
            print("\nCollege Does Not Exist\n")
            print("------------------------------------------------")
            print()

    elif option == 3:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x=True
                break
        if x == True:
            id_no = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            branch = input("Enter Student Branch: ")
            clg.add_student(student(id_no, name, email, branch))
            print(f"\nStudent Added Successfully to {clg.name}\n")
            print("------------------------------------------------")
            print()
        else:
            print("\nCollege Does Not Exist\n")
            print("------------------------------------------------")
            print()

    elif option == 4:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x=True
                break
        if x == True:
            clg.display_teachers()
        else:
            print("\nCollege Does Not Exist\n")
            print("------------------------------------------------")
            print()

    elif option == 5:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x=True
                break
        if x == True:
            clg.display_students()
        else:
            print("\nCollege Does Not Exist\n")
            print("------------------------------------------------")
            print()

    elif option == 6:
        display_colleges(colleges)

    elif option == 7:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x=True
                break
        if x == True:
            student_id = input("Enter Student ID: ")
            for i in range(3):
                subject = input("Enter Subject: ")
                marks = int(input("Enter Marks: "))
                clg.add_marks(student_id, subject, marks)
            print()
        else:
            print("\nCollege Does Not Exist\n")

    elif option == 8:
        clg_id = int(input("Enter College ID: "))
        x = False
        for val in colleges:
            if val.cid == clg_id:
                x=True
                break
        if x==True:
            student_id = input("Enter Student ID: ")
            clg.display_results(student_id)
            print()
        else:
            print("\nCollege Does Not Exist\n")

    elif option == 9:
        print("\nExiting...\n")
        break

    else:
        print("\nWrong Option! Try Again.\n")





                
