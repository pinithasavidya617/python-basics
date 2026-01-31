def grade(mark):
    # 'mark' is just a temporary variable (called a parameter)
    if mark >= 75:
        return "A"
    # ...

sft = 83
ict = 67
et = 45

print(grade(sft))  # 👉 here 'mark' becomes 83
print(grade(ict))  # 👉 now 'mark' becomes 67
print(grade(et))   # 👉 now 'mark' becomes 45
