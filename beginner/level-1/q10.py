'''
input sentence = "Hello World! Welcome to Python Programming"
output after reverse = "Programming. Python to Welcome World! Hello"
'''

def main():
    sentence = input("Enter sentence:")
    words = sentence.split()
    words.reverse()
    reversed_sentence = " ".join(words)
    print("Output after reverse = ",reversed_sentence)

if __name__ == "__main__":
    main()