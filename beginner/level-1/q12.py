'''
reverse a number using while loop
'''
def reverse_number(n):
    n_str = str(n)
    reversed_str = ""
    for i in range(len(n_str)-1,-1,-1):
        reversed_str += n_str[i]
    return int(reversed_str)

def main():
    n = int(input("Enter the number:"))
    reversed_number = reverse_number(n)
    print(f"revnum: {reversed_number}")

if __name__ == "__main__":
    main()