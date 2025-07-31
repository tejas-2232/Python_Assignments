'''
Write a Python program to calculate the sum of digits of a given
number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Final Output: 6
'''

def sum_of_digits(n):
    total = 0
    while n>0:
        digit = n%10
        total = total + digit
        n = n//10
    return total

def main():
    n = int(input("Enter the number:"))
    print(f"Starting with: {n}")
    # Keep calculating sum until we get a single digit
    while n > 9:  # till the number has more than 1 digit
        n = sum_of_digits(n)  # UPDATE n with the new sum
        print(f"Sum of digits: {n}")
    
    print(f"Final Output: {n}")

if __name__ == "__main__":
    main()