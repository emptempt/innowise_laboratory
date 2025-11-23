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
            if 1 <= number <= 5:
                return number
            else:
                print('Please enter a number between 1-5')
        except ValueError:
            print('Please enter a number between 1-5')

def get_grades():
    list_of_grades = list()
    while True:

            number = input("Enter a grade (or 'done' to finish): ")
            try:
                if 0 <= int(number) <= 100:
                    list_of_grades.append(int(number))
                else:
                    print('Please enter a number between 0-100')
            except ValueError:
                if number == 'done':
                    return list_of_grades
                else:
                    print('Please enter a number between 0-100')


def add_grades(n):
    for student in students:
        if n in student:
            student[n].extend(get_grades())
            return
    print(f'Student {n} does not exist')

choises = ('Add a new student', 'Add a grades for student', 'Generate a full report',
               'Find the top student', 'Exit program')
print('--- Student Grade Analyzer ---')
for i, point in enumerate(choises, start=1):
    print(f'{i}. {point}')

while True:
    answer = get_answer()
    if answer == 1:
        name = input('Enter student name: ')
        if any(name in student for student in students):
            print(f'Student {name} already exists!')
        else:
            student = {name: []}
            students.append(student)
    elif answer == 2:
        name = input('Enter student name: ')
        add_grades(name)
    elif answer == 3:
        print('--- Student Report ---')
        avg_grade = []
        for student in students:
            for k,v in student.items():
                try:
                    grade = sum(v)/len(v)
                    avg_grade.append(grade)
                except ZeroDivisionError:
                    grade = 'N/A'
                finally:
                    print(f"{k}'s average grade is {grade}")
        print('-------------------------')
        if not students:
            print('The list does not contain students.')
        elif not avg_grade:
            print('The average grade is N/A')
        else:
            print(f'Max Average: {max(avg_grade)}')
            print(f'Min Average: {min(avg_grade)}')
            print(f'Overall Average: {sum(avg_grade)/len(avg_grade)}')


    elif answer == 4:
        print(f"The student with the highest average grade is {} with grade of {}")
    elif answer == 5:
        print('Exiting program.')
        break
print(students)
