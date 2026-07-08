student_records = []
print("welcome to the Student Data Organizer!")
while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Infromation")
    print("4. Delete Student")
    print("5. Display Subjects offered")
    print("6. Exit")
    choice1 = int(input("Enter your choice: "))

    match choice1:
        case 1:
            print("\nEnter student details:")
            stu_id=int(input("Student ID:"))

            stu_id2 = False
            for student in student_records:
                if student["ID"][0] == stu_id:
                    print("student id is already exists!")
                    break

            else:
                stu_name=input("Name:")
                stu_age=int(input("Age:"))
                stu_grade=input("Grade:")
                stu_DOB=input("Date Of Birth (yyyy-mm-dd): ")
                stu_sub=set(map(str.strip, input("Subjects (comma-separated): ").split(","))) 
                tuple1=(stu_id, stu_DOB)
                student_list={
                    "ID":tuple1,
                    "Name": stu_name,
                    "Age":stu_age,
                    "DOB":tuple1,
                    "Grade":stu_grade,
                    "Subject":stu_sub
                }
                student_records.append(student_list)

                print("\nstudent added successfully!")

        case 2:
            print("\n------Display All Students-----")
            if len(student_records) == 0:
                print("student data is not found!")
            else:
                for student in student_records:
                    print(f"Student ID : {student['ID'][0]} | Name : {student['Name']} | Age : {student['Age']} | Grade : {student['Grade']} | DOB : {student['DOB'][1]} | Subjects : {', '.join(student['Subject'])}")        
        case 3:
            print("------Update Student Information-----")
            stu_id = int(input("enter student ID:"))
            for student2 in student_records:
                if student2["ID"][0] == stu_id:
                    print("1. update age")
                    print("2. add subject")

                    update_choice = int(input("Enter Your choice(1-2):"))
                    if update_choice == 1:
                        new_age = int(input("enter New Age: ")) 
                        if new_age <= 0:
                            print("Invalid Age!")
                        else:
                            student2["Age"] = new_age
                            print("\nAge is updated successfully!")
                            break

                    elif update_choice == 2:
                        new_sub=set(map(str.strip, input("enter new subject: ").split(",")))
                        student2["Subject"].update(new_sub)
                        print("\nsubject is added successfully!")
                        break
                    else:
                        print("Invalid choice!")
            else:
               print("student id not found!")

        case 4:
            print("------Delete Student Record-----")
            stu_id=int(input("enter id:"))
            for s in range(len(student_records)):
                if student_records[s]["ID"][0] == stu_id:
                    del student_records[s]
                    print("\nstudent deleted successfully!")
                    break
            else:
                print("Student ID not found!")

        case 5:
            print("------Display Subjects Offered-----")
            all_subjects = set()
            for student2 in student_records:
                all_subjects.update(student2["Subject"])
            
            if all_subjects:
                print(", ".join(all_subjects))
            else:
                print("No subjects offered yet.")
        case 6:
            print("Thank you for using Student Data Organizer!")
            break
        case _:
            print("Invalid choice! please select between 1-6.")
