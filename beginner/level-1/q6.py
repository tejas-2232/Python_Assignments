'''
Write a Python program to check if a given number is a perfect
number.
A Perfect number is a positive integer that is equal to the sum of
its proper divisors. 
For instance, 6 has divisors 1, 2, and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number
'''

def perfect_number(n):
    if n < 1:
        return False
    sum_of_divisors = 1

    for i in range(1,n):
        if n%i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n


def main():
    n = int(input("enter the number:"))
    if perfect_number(n):
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")