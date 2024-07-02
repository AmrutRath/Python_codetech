def calculate_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(letter_grade):
    gpa_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return gpa_scale.get(letter_grade, 0.0)

def input_grades(grades):
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
                continue
            grades[subject] = grade
        except ValueError:
            print("Invalid input. Please enter a number.")
    return grades

def update_grade(grades):
    subject = input("Enter the subject name you want to update: ")
    if subject in grades:
        try:
            grade = float(input(f"Enter new grade for {subject}: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
            else:
                grades[subject] = grade
                print(f"Grade updated for {subject}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print(f"No grades found for {subject}.")

def remove_grade(grades):
    subject = input("Enter the subject name you want to remove: ")
    if subject in grades:
        del grades[subject]
        print(f"Grade removed for {subject}.")
    else:
        print(f"No grades found for {subject}.")

def calculate_average(grades):
    return sum(grades.values()) / len(grades) if grades else 0

def display_results(grades):
    if not grades:
        print("No grades to display.")
        return
    
    average = calculate_average(grades)
    letter_grade = calculate_letter_grade(average)
    gpa = calculate_gpa(letter_grade)
    
    print("\nGrade Summary:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

def main():
    print("Welcome to the Student Grade Tracker!")
    grades = {}
    
    while True:
        print("\nMenu:")
        print("1. Input Grades")
        print("2. Update Grade")
        print("3. Remove Grade")
        print("4. Display Results")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            grades = input_grades(grades)
        elif choice == '2':
            update_grade(grades)
        elif choice == '3':
            remove_grade(grades)
        elif choice == '4':
            display_results(grades)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
