'''
Write a Python program to find the sum of all odd numbers
between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25
'''

def main():
    start_num = int(input("Enter the start number:"))
    end_num = int(input("Enter the end number:"))

    sum =0
    for i in range(start_num, end_num + 1):
        if i%2 !=0:
            sum = sum + i
    print("Sum of odd numbers:",sum)
    
if __name__ == "__main__":
    main()