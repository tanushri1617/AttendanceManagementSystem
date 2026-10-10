Attendance Management System

Introduction

The Attendance Management System is a Python-based application designed to manage student attendance records efficiently. It helps users maintain student details, record daily attendance, and calculate attendance percentages.

Objectives

- To maintain student records.
- To mark and update student attendance.
- To view attendance records date-wise.
- To calculate individual attendance percentages.
- To calculate the average attendance of the class.
- To store attendance data permanently using JSON.

Technologies Used

- Programming Language: Python
- Data Storage: JSON
- Code Editor: Visual Studio Code
- Libraries: "json", "os", "datetime"

Features

1. Add students using roll numbers and names.
2. View all registered students.
3. Mark and update attendance.
4. View date-wise attendance records.
5. Calculate individual attendance percentages.
6. Check attendance status for a specific date.
7. Delete attendance records.
8. Calculate the class average attendance percentage.
9. Save student and attendance information in a JSON file.

Project Structure

AttendanceManagementSystem/
├── main.py
├── students.json
├── test_ai.py
├── .env
├── .gitignore
└── README.md

Installation and Execution

Prerequisites

- Python 3 installed
- Visual Studio Code

Steps to Run

1. Open the project folder in Visual Studio Code.
2. Open the integrated terminal.
3. Run the following command:

python main.py

4. Select an option from the menu to perform the required operation.

Data Storage

The application stores student information and attendance records in "students.json". The data remains available after the program is closed and can be accessed when the program runs again.

AI Integration Testing

The project includes "test_ai.py" to test connectivity with the Hugging Face AI service. The test requires the necessary Python packages and a valid Hugging Face API token configured through an environment file.

Run the AI test using:

python test_ai.py

Attendance Percentage Formula

Attendance percentage is calculated using the following formula:

Attendance Percentage = (Number of Present Days / Total Recorded Days) × 100

Advantages

- Simple and easy to use.
- Reduces manual attendance record-keeping.
- Provides quick access to attendance information.
- Stores records for future reference.
- Calculates attendance percentages automatically.

Future Scope

- Graphical user interface.
- Database integration.
- User login and authentication.
- Exportable attendance reports.
- Automated attendance through QR codes.

Conclusion

The Attendance Management System demonstrates the practical application of Python programming, functions, dictionaries, conditional statements, loops, file handling, and JSON data storage. It provides a simple way to manage student attendance and generate basic attendance statistics.