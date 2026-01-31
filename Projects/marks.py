def grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 55:
        return "C"
    elif marks >= 35:
        return "S"
    else:
        return "W"

for student in range(1, 4):
    print(f"Student {student}")
    sft = int(input("Enter your SFT marks: "))
    ict = int(input("Enter your ICT marks: "))
    et = int(input("Enter your ET marks: "))
    print(f"Student {student} Results -> SFT: {grade(sft)}, ICT: {grade(ict)}, ET: {grade(et)} ")


