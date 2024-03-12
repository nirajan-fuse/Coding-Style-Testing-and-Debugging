"""
Module: coding_conventions.py

This module provides an example of following PEP8 guidelines.
"""

# Create a Python program that manages student records. The program should have
# the following functionalities:
# Create a function that can add new students to the records with their
# student_id, name, age, and grade. The records should be saved to “json” file
# and each time new record is added, it should be saved to same “json” file
# Allow searching for a student by student_id or name. The data should return
# age and grade from the saved file.
# Allow updating a student's information by using student_id or name(age or
# grade)
# Ensure to follow PEP8 Coding Guidelines for following criterias:
# -Proper Indentation
# -Maximum Line Length
# -Prescriptive Naming conventions (Package and Module Names, Class Names,
# Exception Names, Global Variable Names, Function and Variable Names, Method
# Names and Instance Variables, Constants)
# -Source File Encoding while accessing the JSON file
# -Add NumPy Docstring  to each function

import json


class StudentManager:
    """Manage student records."""

    def __init__(self, file_path="./student_records.json"):
        """
        Initialize the StudentRecordManager with the file path of the JSON file.

        Args:
            file_path (str): The path to the JSON file.
        """
        self.file_path = file_path

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student to the records.

        Args:
            student_id (int): The student's ID.
            name (str): The student's name.
            age (int): The student's age.
            grade (str): The student's grade.

        Returns:
            None
        """
        record = {
            "Student_Id": student_id,
            "Name": name,
            "Age": age,
            "Grade": grade,
        }
        try:
            with open(self.file_path, encoding="UTF-8", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(self.file_path, encoding="UTF-8", mode="w") as file:
                json.dump([record], file, indent=4)
                return

        data.append(record)
        with open(self.file_path, encoding="UTF-8", mode="w") as file:
            json.dump(data, file, indent=4)

    def search_student(self, search_key):
        """
        Search for a student by student_id or name.

        Args:
            search_key (str): The student_id or name to search for.

        Returns:
            dict: The student's information (age and grade) if found, None otherwise.
        """
        try:
            with open(self.file_path, encoding="UTF-8", mode="r") as file:
                records = json.load(file)
                for record in records:
                    if search_key in (record["Student_Id"], record["Name"]):
                        return {"Age": record["Age"], "Grade": record["Grade"]}
            return None
        except FileNotFoundError:
            return None

    def update_student(self, search_key, field, value):
        """
        Update a student's information.

        Args:
            search_key (str): The student_id or name to search for.
            field (str): The field to update (age or grade).
            value (str): The new value for the field.

        Returns:
            bool: True if the student's information was updated successfully, False otherwise.
        """
        updated = False
        try:
            with open(self.file_path, encoding="UTF-8", mode="r") as file:
                records = json.load(file)
        except FileNotFoundError:
            return False

        temp_records = records.copy()
        for i, record in enumerate(records):
            if search_key in (record["Student_Id"], record["Name"]):
                temp_records[i][field] = value
                updated = True
                break
        if updated:
            with open(self.file_path, encoding="UTF-8", mode="w") as file:
                json.dump(temp_records, file, indent=4)
        return updated


manager = StudentManager()
manager.add_student(1, "Nirajan", 24, "A")
manager.add_student(2, "Chandan", 23, "B")

result = manager.search_student("Nirajan")

if result:
    print("Age:", result["Age"])
    print("Grade:", result["Grade"])
else:
    print("Student not found.")

if manager.update_student(1, "Age", 19):
    print("Student age updated successfully.")
else:
    print("Failed to update student's age.")
