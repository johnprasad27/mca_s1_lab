import csv

with open("sample.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row[0],row[2])