# College Management System

## 📌 Project Description

The **College Management System** is a Python-based console application designed to manage students, teachers, and colleges efficiently. It allows users to create colleges, add students and teachers, assign marks, and display results using Object-Oriented Programming (OOP) principles.

This project simulates a simple college management system where users can perform various operations, including:
- Registering colleges
- Adding students and teachers
- Assigning marks to students
- Displaying student results
- Implementing OTP-based verification for secure teacher registration

## 🚀 Features

- **College Management:** Create and store multiple colleges with unique IDs.
- **Student Management:** Add students, assign them to a college, and update their marks.
- **Teacher Management:** Add teachers and associate them with subjects.
- **OTP Verification:** Secure teacher registration using OTP authentication.
- **Marks Management:** Assign marks to students and calculate their average scores.
- **Result Display:** View student marks and calculate their average performance.
- **Console-based Interface:** Easy-to-use menu-driven system.

## 🛠️ Technologies Used

- **Python** (Core Logic & OOP)
- **Random Module** (OTP Generation)
- **Basic Data Structures** (Lists & Dictionaries)

## 📂 Project Structure

```
📁 College Management System
│── main.py        # Main application file
│── README.md      # Project documentation
```

## 🏃‍♂️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/college-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd college-management-system
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## 📌 Usage Instructions

1. **Create a College**
   - Select option `1` to create a new college.
   - Enter the college ID, name, and location.
   - The college will be stored in the system.

2. **Add a Teacher**
   - Select option `2` to add a teacher.
   - Enter teacher details (ID, Name, Email, Subject).
   - OTP verification will be required to complete registration.

3. **Add a Student**
   - Select option `3` to register a student.
   - Provide student details (ID, Name, Email, Branch).
   - The student will be added to the selected college.

4. **View Details**
   - Use options `4` and `5` to display teacher and student details for a given college.
   - Use option `6` to display all registered colleges.

5. **Manage Marks & Results**
   - Select option `7` to assign marks to a student.
   - Select option `8` to display the results of a student.

6. **Exit**
   - Choose option `9` to exit the system.

## 💡 Future Enhancements

- Implement a **GUI** version using Tkinter or Flask.
- Store data in a **database** instead of lists.
- Add **authentication** for different user roles (Admin, Teacher, Student).
- Include **report generation** for student performance analysis.
- Implement **email-based OTP verification** instead of random OTP.

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the project, feel free to:
- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request
