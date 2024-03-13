"""
This script filters data from 'data.csv' and writes it to 'adult.csv' if
the age is 18 or above.
"""

# Implement a program that reads a CSV file named "data.csv,"
# containing columns "Name" and "Age." Create a new CSV file called
# "adults.csv" with only the rows of individuals who are 18 years or
# older.

import csv

with open("data.csv", encoding="UTF-8") as file:
    datas = csv.DictReader(file)

    with open("adult.csv", "a", encoding="UTF-8") as sub_file:
        writer = csv.DictWriter(sub_file, fieldnames=["Name", "Age"])

        for data in datas:
            if int(data["Age"]) >= 18:
                writer.writerow({"Name": data["Name"], "Age": data["Age"]})
