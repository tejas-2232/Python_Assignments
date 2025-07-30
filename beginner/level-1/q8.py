'''
Write a Python program to calculate the LCM (Least Common
Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36
'''

def main():
    num1 = int(input("Enter the number 1:"))
    num2 = int(input("Enter the number 2:"))

    max_num = max(num1, num2)

    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            lcm = max_num
            break
        max_num += 1

    print(f"LCM of {num1} and {num2} are: {lcm}")
if __name__ == "__main__":
    main()