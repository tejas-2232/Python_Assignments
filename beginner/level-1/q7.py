'''
Write a Python program to check if a string is an anagram of
another string.
string1 = "listen", string2 = "silent"
Output: True

'''

def main():
    string1 = input("Enter the string 1:")
    string2 = input("Enter the string 2:")


    if len(string1) != len(string2):
        print("False")
    else:
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)

        if sorted_string1 == sorted_string2:
            print("True")
        else:
            print("False")

if __name__ == "__main__":
    main()