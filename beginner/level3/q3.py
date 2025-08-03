
def JtoI(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            content = content.replace("J", "I").replace("j", "i")
            return content
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    file_path = "words.txt"
    print(JtoI(file_path))
