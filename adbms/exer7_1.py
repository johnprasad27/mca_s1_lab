import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
db=conn['college']
col=db['studlist']

# --------------------------------------------------
# 1. display fname lname and mark of all female MCA students
# --------------------------------------------------

print("\n1. Female MCA Students")

x = db.studlist.find(
    {"gender":"female","course":"MCA"},
    {"name":1,"mark":1,"_id":0}
)

for i in x:
    print(
        "\nName:",
        i["name"]["fname"]+" "+i["name"]["lname"],
        "\nMark:",
        i["mark"]
    )


# --------------------------------------------------
# 2. highest mark in MCA
# --------------------------------------------------

print("\n2. Highest Mark in MCA")

x = db.studlist.find(
    {"course":"MCA"}
).sort("mark",-1).limit(1)

for i in x:
    for j in i.keys():
        print(j,":",i[j])


# --------------------------------------------------
# 3. male students with A+ grade
# --------------------------------------------------

print("\n3. Male Students with A+ Grade")

x = db.studlist.find(
    {"grade":"A+","gender":"male"}
)

for i in x:
    print(i['name']['fname']+" "+i['name']['lname'])


# --------------------------------------------------
# 4. top three students in mechanical department
# --------------------------------------------------

print("\n4. Top Three Mechanical Students")

x = db.studlist.find(
    {"department":"Mechanical"}
).sort("mark",-1).limit(3)

for i in x:
    print(
        i['name']['fname'],
        i['name']['lname'],
        "-",
        i['mark']
    )


# --------------------------------------------------
# 5. female students with mark > 90
# --------------------------------------------------

print("\n5. Female Students with Mark > 90")

x = db.studlist.find(
    {"gender":"female","mark":{"$gt":90}},
    {"name":1,"grade":1,"mark":1,"contact":1,"_id":0}
)

for i in x:
    print(
        "\nName:",
        i["name"]["fname"]+" "+i["name"]["lname"],
        "\nGrade:",
        i["grade"],
        "\nMark:",
        i["mark"],
        "\nContact:",
        i["contact"]
    )


# --------------------------------------------------
# 6. mark between 80 and 90
# --------------------------------------------------

print("\n6. Students with Mark between 80 and 90")

x = db.studlist.find(
    {"mark":{"$gt":80,"$lt":90}}
)

for i in x:
    print(
        i["name"]["fname"],
        i["name"]["lname"],
        "-",
        i["mark"]
    )


# --------------------------------------------------
# 7. names starting with V
# --------------------------------------------------

print("\n7. Students whose names start with V")

x = db.studlist.find(
    {"name.fname":{"$regex":"^V"}}
)

for i in x:
    print(i["name"]["fname"],i["name"]["lname"])


# --------------------------------------------------
# 8. students from Kollam
# --------------------------------------------------

print("\n8. Students from Kollam")

x = db.studlist.find(
    {"place":"Kollam"}
)

for i in x:
    print(i["name"]["fname"],i["name"]["lname"])


# --------------------------------------------------
# 9. students not from Kollam or Thiruvananthapuram
# --------------------------------------------------

print("\n9. Students not from Kollam or Thiruvananthapuram")

x = db.studlist.find(
    {"place":{"$nin":["Kollam","Thiruvananthapuram"]}}
)

for i in x:
    print(
        i["name"]["fname"],
        i["name"]["lname"],
        "-",
        i["place"]
    )