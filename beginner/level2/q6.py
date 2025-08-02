'''
Write a Python program to check if a number is a power of two
using recursion.
'''

def power_of_two(n):
    # Base case: 1 = 2^0
    if n == 1:
        return True
    
    # Base case: numbers <= 0 or odd numbers (except 1) are not powers of 2
    if n <= 0 or n % 2 != 0:
        return False
    
    # Recursive case: divide by 2 and check again
    return power_of_two(n // 2)

def main():
    num = int(input("Enter a number: "))
    
    if power_of_two(num):
        print(f"{num} is a power of two")
    else:
        print(f"{num} is not a power of two")
    
    
if __name__ == "__main__":
    main()
