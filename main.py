import json
import os
from datetime import date

DATA_FILE = "students.json"


def load_students():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read students.json.")
    return {}


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    roll = input("Roll number: ").strip()
    if not roll or roll in students:
        print("Invalid or existing roll number.")
        return

    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    students[roll] = {"name": name, "attendance": {}}
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for roll, student in students.items():
        print(f"{roll} - {student['name']}")


def mark_attendance(students):
    roll = input("Roll number: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    day = input("Date (YYYY-MM-DD, Enter for today): ").strip()
    day = day or date.today().isoformat()

    try:
        date.fromisoformat(day)
    except ValueError:
        print("Invalid date format.")
        return

    old = students[roll]["attendance"].get(day)
    if old:
        print("Existing attendance:", old)

    status = input("P = Present, A = Absent: ").strip().upper()
    if status not in ("P", "A"):
        print("Invalid status.")
        return

    students[roll]["attendance"][day] = (
        "Present" if status == "P" else "Absent"
    )
    save_students(students)
    print("Attendance saved.")


def view_attendance(students):
    roll = input("Roll number: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]
    records = student["attendance"]

    print(f"\nAttendance: {student['name']}")
    if not records:
        print("No attendance records.")
        return

    for day, status in sorted(records.items()):
        print(day, "-", status)

    total = len(records)
    present = sum(s == "Present" for s in records.values())
    print(f"Present: {present}, Absent: {total - present}")
    print(f"Percentage: {present / total * 100:.2f}%")


def check_date(students):
    roll = input("Roll number: ").strip()
    day = input("Date (YYYY-MM-DD): ").strip()

    if roll not in students:
        print("Student not found.")
        return

    status = students[roll]["attendance"].get(day)
    print(f"{day}: {status if status else 'No record found'}")


def remove_attendance(students):
    roll = input("Roll number: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    day = input("Date (YYYY-MM-DD): ").strip()
    records = students[roll]["attendance"]

    if day not in records:
        print("Attendance record not found.")
        return

    del records[day]
    save_students(students)
    print("Attendance record removed.")


def class_average(students):
    percentages = []

    for student in students.values():
        records = student["attendance"]
        if records:
            present = sum(s == "Present" for s in records.values())
            percentages.append(present / len(records) * 100)

    if percentages:
        print(f"Class average attendance: "
              f"{sum(percentages) / len(percentages):.2f}%")
    else:
        print("No attendance records available.")


def main():
    students = load_students()

    while True:
        print("\n=== ATTENDANCE MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark / Update Attendance")
        print("4. View Attendance and Percentage")
        print("5. Check Attendance on a Date")
        print("6. Remove Attendance Record")
        print("7. Calculate Class Average")
        print("8. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            mark_attendance(students)
        elif choice == "4":
            view_attendance(students)
        elif choice == "5":
            check_date(students)
        elif choice == "6":
            remove_attendance(students)
        elif choice == "7":
            class_average(students)
        elif choice == "8":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()