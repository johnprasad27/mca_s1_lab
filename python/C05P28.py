import csv
with open(r"c:/Users/john27/MCA/mca_s1/lab/python/data.csv","r")as file:
  reader = csv.reader(file)

  for row in reader:
    print(row)