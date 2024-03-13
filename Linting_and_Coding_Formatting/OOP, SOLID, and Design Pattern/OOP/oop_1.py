"""
This module contains classes to represent a University and its Departments.
"""

# Create a Python class to represent a University. The university should have
# attributes like name, location, and a list of departments. Implement
# encapsulation to protect the internal data of the University class. Create a
# Department class that inherits from the University class. The Department
# class should have attributes like department name, head of the department,
# and a list of courses offered. Implement polymorphism by defining a common
# method for both the University and Department classes to display their
# details.


class University:
    """
    Represents a university with a name, location, and departments.

    Attributes:
        name (str): The name of the university.
        location (str): The location of the university.
        departments (list): A list of department names within the university.

    Methods:
        display_details(): Displays the details of the university, including
        its name, location, and departments.
    """

    def __init__(self, name, location, departments):
        """
        Initializes a University object with the given name, location, and
        departments.

        Args:
            name (str): The name of the university.
            location (str): The location of the university.
            departments (list): A list of department names within the
            university.
        """
        self._name = name
        self._location = location
        self._departments = departments

    def display_details(self):
        """
        Displays the details of the university.

        Prints:
            University Name: [name]
            Location: [location]
            Departments:
            - [department1]
            - [department2]
            ...
        """
        print("University Name:", self._name)
        print("Location:", self._location)
        print("Departments:")
        for dep in self._departments:
            print("-", dep)


class Department(University):
    """
    Represents a department within a university.

    Inherits from University.

    Attributes:
        name (str): The name of the university.
        location (str): The location of the university.
        dep_name (str): The name of the department.
        hod (str): The head of the department.
        courses (list): A list of courses offered by the department.

    Methods:
        display_details(): Displays the details of the department, including
        its name, head, and courses offered.
    """

    def __init__(self, name, location, dep_name, hod, courses):
        """
        Initializes a Department object with the given attributes.

        Args:
            name (str): The name of the university.
            location (str): The location of the university.
            dep_name (str): The name of the department.
            hod (str): The head of the department.
            courses (list): A list of courses offered by the department.
        """
        super().__init__(name, location)
        self._dep_name = dep_name
        self._hod = hod
        self._courses = courses

    def display_details(self):
        """
        Displays the details of the department.

        Prints:
            Department Name: [department_name]
            Head of Department: [hod]
            Courses Offered:
            - [course1]
            - [course2]
            ...
        """
        print("Department Name:", self._dep_name)
        print("Head of Department:", self._hod)
        print("Courses Offered:")
        for course in self._courses:
            print("-", course)


university = University(
    name="Tribhuvan University", location="Kathmandu", departments=["CSIT", "BE"]
)

department = Department(
    name="Tribhuvan University",
    location="Kathmandu",
    dep_name="CSIT",
    hod="Ram Thapa",
    courses=["C Programming", "Microprocessor"],
)

university.display_details()
print()
department.display_details()
