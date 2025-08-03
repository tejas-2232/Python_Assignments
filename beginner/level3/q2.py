'''
Write a program to count the lines in a file “demo.txt
'''

def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    file_path = "doc.txt"
    print(count_lines(file_path))
