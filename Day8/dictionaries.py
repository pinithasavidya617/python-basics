student = {
    "name" : "Test",
    "age" : 20,
    "married" : True,
    "address" : "Test",
    "contact" : ["07777777777"]
}

print(student["name"])

student["name"] = "Kalana"

print(student["name"])

student["grades"] = 'TEST'
print(student)

if "grades" in student: #do a validation helps to reduce key errors
    print(student["grades"])


student["contact"].append("0775554566")
for num in student["contact"]:
    print(num)