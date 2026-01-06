import csv

data = [
    {"Name": "John", "Age": 21, "City": "Kochi"},
    {"Name": "Anna", "Age": 22, "City": "Trivandrum"},
    {"Name": "Sam", "Age": 20, "City": "Calicut"}
]

with open("output.csv","w",newline="") as file:
    writer=csv.DictWriter(file,fieldnames=data[0].keys())
    writer.writeheader()

    for row in data:
        writer.writerow(row)             #or use writerows(data)

with open("output.csv","r") as file:
    reader=csv.reader(file)
    for row in file:
        print(row)
