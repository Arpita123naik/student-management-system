import json
import os

FILE_NAME = "students.json"

# Load data from file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    name = input("Enter student name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()

    if not name or not age or not course:
        print("❌ All fields are required!\n")
        return

    if not age.isdigit():
        print("❌ Age must be a number!\n")
        return

    students.append({
        "name": name,
        "age": int(age),
        "course": course
    })

    save_data(students)
    print("✅ Student added successfully!\n")

# View students
def view_students(students):
    if not students:
        print("📭 No students found.\n")
        return

    print("\n📋 Student List:")
    print("-" * 40)
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Course: {s['course']}")
    print()

# Search student
def search_student(students):
    name = input("Enter name to search: ").strip().lower()

    results = [s for s in students if name in s["name"].lower()]

    if results:
        print("\n🔍 Results:")
        for s in results:
            print(f"{s['name']} | Age: {s['age']} | Course: {s['course']}")
        print()
    else:
        print("❌ No matching student found.\n")

# Delete student
def delete_student(students):
    name = input("Enter name to delete: ").strip().lower()

    for s in students:
        if s["name"].lower() == name:
            students.remove(s)
            save_data(students)
            print("🗑️ Student deleted successfully!\n")
            return

    print("❌ Student not found.\n")

# Main menu
def main():
    students = load_data()

    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!\n")

if __name__ == "__main__":
    main()
