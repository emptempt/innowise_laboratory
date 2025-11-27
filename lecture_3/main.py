# Initialize an empty list to store student data
students = list()

def get_answer():
    """
    Get integer input from user in range 1-5 with validation.

    Returns:
        int: Valid number between 1-5
    """
    while True:
        try:
            number = int(input('Enter your choice: '))
            # Validate number between 1-5
            if 1 <= number <= 5:
                return number
            else:
                print('Please enter a number between 1-5')
        except ValueError:
            print('Please enter a number between 1-5')

def get_grades():
    """
    Collect grades from user input with validation.

    Returns:
        list: List of grades
    """
    list_of_grades = list()
    while True:

            number = input("Enter a grade (or 'done' to finish): ")
            try:
                # Validate grade is between 0-100
                if 0 <= int(number) <= 100:
                    list_of_grades.append(int(number))
                else:
                    print('Please enter a number between 0-100')
            except ValueError:
                # Check if user wants to finish input
                if number == 'done':
                    return list_of_grades
                else:
                    print('Please enter a number between 0-100')

def add_grades(n):
    """
    Add grades to an existing student.

    Args:
         n(str): Name of student
    """
    # Search for student in the list
    for student in students:
        if n in student:
            # Extend existing grades with new ones
            student[n].extend(get_grades())
            return
    # Student not found
    print(f'Student {n} does not exist')

# Define menu options
choises = ('Add a new student', 'Add a grades for student', 'Generate a full report',
               'Find the top student', 'Exit program')

# Display program header
print('--- Student Grade Analyzer ---')

# Display menu options
for i, point in enumerate(choises, start=1):
    print(f'{i}. {point}')

# Main program loop
while True:
    answer = get_answer()

    # Option 1: Add new student
    if answer == 1:
        name = input('Enter student name: ').title() # Capitalize name
        # Check if student already exists
        if any(name in student for student in students):
            print(f'Student {name} already exists!')
        else:
            # Create new student dictionary and add to list
            student = {name: []}
            students.append(student)

    # Option 2: Add grades for existing student
    elif answer == 2:
        name = input('Enter student name: ').title() # Capitalize name
        add_grades(name)

    # Option 3: Generate report
    elif answer == 3:
        print('--- Student Report ---')
        # Store average grades for each student
        avg_grade = []
        for student in students:
            for k,v in student.items():
                grade = 0
                try:
                    # Calculate average grade
                    grade = sum(v)/len(v)
                    avg_grade.append(grade)
                except ZeroDivisionError:
                    # Handle case when student has no grades
                    grade = 'N/A'
                finally:
                    # Display student's average
                    if grade == 'N/A':
                        print(f"{k}'s average grade is {grade}")
                    else:
                        print(f"{k}'s average grade is {grade:.2f}")
        print('-------------------------')

        # Display statistics
        if not students:
            print('The list does not contain students.')
        elif not avg_grade:
            print('The average grade is N/A')
        else:
            # Display msx, min and overall averages
            print(f'Max Average: {max(avg_grade):.2f}')
            print(f'Min Average: {min(avg_grade):.2f}')
            print(f'Overall Average: {(sum(avg_grade)/len(avg_grade)):.2f}')

    # Option 4: Find student with the highest average grade
    elif answer == 4:
        if students:
            # Find student with the highest average grade
            top_student = max(students, key=lambda x: sum(list(x.values())[0])/sum(list(x.values())[0]) if list(x.values())[0] else 0)
            student_name = list(top_student.keys())[0]
            student_grade = list(top_student.values())[0]

            if student_grade:
                # Calculate and display average grade
                average_grade = sum(student_grade)/len(student_grade)
                print(f"The student with the highest average grade is {student_name} with grade of {average_grade:.2f}")
            else:
                print("Students have no grade yet.")
        else:
            print("No students in the list.")

    # Option 5: Exit the program
    elif answer == 5:
        print('Exiting program.')
        break

