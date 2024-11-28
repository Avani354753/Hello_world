# project 1
# Student Management system

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

def find_max_min(numbers):
    """Find the maximum and minimum values in a list."""
    return max(numbers), min(numbers)

# Dictionary to store student information
students = {}

# Main program
while True:
    print("\n1. Add student")
    print("2. View student")
    print("3. Calculate class average")
    print("4. Exit")

    choice = input("Enter your choice (1-4):")

    if choice == '1':
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        students[name] = score
        print(f"Added {name} with score {score}")

    elif choice == '2':
        name = input("Enter student name to view: ")
        if name in students:
            print(f"{name}'s score: {students[name]}")
        else:
            print("Student not found")

    elif choice == '3':
        if students:
            scores = list(students.values())
            avg = calculate_average(scores)
            max_score, min_score = find_max_min(scores)
            print(f"Class average: {avg:.2f}")
            print(f"Highest score: {max_score}")
            print(f"Lowest score: {min_score}")
        else:
            print("No students added yet")

    elif choice == '4':
        print("Existing program")
        break

    else:
        print("Invalid choice. Please try again")

