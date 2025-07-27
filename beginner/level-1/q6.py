'''
Write a Python program to check if a given number is a perfect
number.
A Perfect number is a positive integer that is equal to the sum of
its proper divisors. 
For instance, 6 has divisors 1, 2, and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number
'''

def is_perfect_number(n):
    if n < 1:
        return False

    sum_of_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

def main():
    try:
        n = int(input("Enter the number: "))
        if is_perfect_number(n):
            print("No")
        else:
            print("Yes")
    except ValueError:
        print("Invalid entry. Enter a valid integer.")

if __name__ == "__main__":
    main()