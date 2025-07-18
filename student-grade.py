grades = {}

while True:
    print("\n--- Student Grade Menu ---")
    print("1. Add new student and grade")
    print("2. Update existing student’s grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in grades:
            print("Student already exists.")
        else:
            grade = input("Enter grade: ")
            grades[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        if grades:
            print("\nAll Student Grades:")
            for student, grade in grades.items():
                print(f"{student}: {grade}")
        else:
            print("No student records found.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
