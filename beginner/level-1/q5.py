'''
find factorial of a number
'''
def main():
    n = int(input("Enter the number:"))
    fact = 1
    if n == 0 or n==1:
        print("Factorial of",n,"is",fact)
    else:   
        for i in range(1,n+1):
            fact = fact * i
        print("Factorial of",n,"is",fact)

if __name__ == "__main__":
    main()