import csv
csv_path = r"C:\Users\john27\MCA\mca_s1\lab\python\data.csv"
data = [
    {"Name": "John", "Age": "25", "Job": "Engineer"},
    {"Name": "Alice", "Age": "30", "Job": "Designer"},
    {"Name": "Bob", "Age": "22", "Job": "Student"}
]
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Job"])
    writer.writeheader()
    writer.writerows(data)
with open(csv_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))