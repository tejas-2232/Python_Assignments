'''
Write a program that accepts a string as input from the user and
calculates the number of digits and letters
'''
def main():
    user_input = input("enter the string: ")
    alpha_count = 0
    num_count = 0

    for i in user_input:
        if i.isdigit():
            num_count +=1

    for i in user_input:        
        if i.isalpha():
            alpha_count +=1
    print("Alphabet:",alpha_count, "& Number:", num_count )


if __name__ == "__main__":
    main()

