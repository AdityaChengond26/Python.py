Subject = {
    "Name"    : "Python",
    "Chapter" : 5,
    "Time"    : "21hrs",
}
print(Subject)

print(Subject["Name"])

Subject["Time"]="35hrs"
Subject["Students"]=32
print(Subject)

del Subject["Chapter"]
print(Subject)
