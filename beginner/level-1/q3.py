'''
Write a Python program to input marks for five subjects Physics,
Chemistry, Biology, Mathematics, and Computer. Calculate the
percentage and grade according to the following:

Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
'''
def main():
    physics = int(input("Enter physics marks:"))
    chem = int(input("Enter Chemistry marks:"))
    bio = int(input("Enter Biology marks:"))
    maths = int(input("Enter Mathematics marks:"))
    comp = int(input("Enter computer marks:"))

    total = physics + chem + bio + maths + comp
    percentage = (total / 500) * 100

    if percentage >= 90:
        print("Grade A")
    elif percentage >= 80:
        print("Grade B")
    elif percentage >= 70:
        print("Grade C")
    elif percentage >= 60:
        print("Grade D")
    elif percentage >= 40:
        print("Grade E")
    else:
        print("Grade F")

if __name__ == "__main__":
    main()
