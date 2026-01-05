import json


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self):
        try:
            roll = int(input("Enter roll number: "))

            for s in self.students:
                if s["roll"] == roll:
                    print("Roll number already exists!")
                    return

            name = input("Enter name: ")
            marks = int(input("Enter marks (0-100): "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100")
                return

            self.students.append({
                "roll": roll,
                "name": name,
                "marks": marks
            })
            self.save_data()
            print("Student added successfully")

        except ValueError:
            print("Invalid input")

    def list_students(self):
        if not self.students:
            print("No students found")
            return

        print("\n--- Student List ---")
        for s in self.students:
            print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")

    def search_student(self):
        try:
            roll = int(input("Enter roll number to search: "))
            for s in self.students:
                if s["roll"] == roll:
                    print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")
                    return
            print("Student not found")
        except ValueError:
            print("Invalid roll number")

    def update_student(self):
        try:
            roll = int(input("Enter roll number to update: "))
            for s in self.students:
                if s["roll"] == roll:
                    s["name"] = input("Enter new name: ")
                    marks = int(input("Enter new marks: "))

                    if marks < 0 or marks > 100:
                        print("Marks must be between 0 and 100")
                        return

                    s["marks"] = marks
                    self.save_data()
                    print("Student updated successfully")
                    return
            print("Student not found")
        except ValueError:
            print("Invalid input")

    def delete_student(self):
        try:
            roll = int(input("Enter roll number to delete: "))
            new_students = [s for s in self.students if s["roll"] != roll]

            if len(new_students) == len(self.students):
                print("Student not found")
            else:
                self.students = new_students
                self.save_data()
                print("Student deleted successfully")
        except ValueError:
            print("Invalid roll number")

    def stats(self):
        if not self.students:
            print("No data available")
            return

        marks = [s["marks"] for s in self.students]
        print("Average Marks:", sum(marks) / len(marks))
        print("Highest Marks:", max(marks))
        print("Lowest Marks:", min(marks))


def main():
    manager = StudentManager()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                manager.add_student()
            case "2":
                manager.list_students()
            case "3":
                manager.search_student()
            case "4":
                manager.update_student()
            case "5":
                manager.delete_student()
            case "6":
                manager.stats()
            case "7":
                print("Exiting... Bye ")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
