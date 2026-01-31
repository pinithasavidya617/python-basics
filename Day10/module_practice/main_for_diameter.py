import calculator

def main():
    num = int(input("Enter radius: "))
    diameter = calculator.calculate_circle_diameter(num)
    print(diameter)

while True:
    main()