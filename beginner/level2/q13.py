'''
lambda function is used to create anonymous functions

lambda arguments: expression
arguments: zero or more comma-separated param
expression- single python expression

lambda functions are used when you need a function for a short period of time
'''

'''
question: Write a Python program to find if a given string starts with a
given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H"
Sample Output: True
'''
def check_string_start(input_string, given_char):
    return lambda input_string: input_string.startswith(given_char)


if __name__ == "__main__":
    input_string = input("enter string:")
    given_char = input("enter character:")
    result = check_string_start(input_string, given_char)
    print(result(input_string))