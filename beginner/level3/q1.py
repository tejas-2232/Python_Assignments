def even_length_str(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            even_length_words = [word for word in words if len(word) % 2 == 0]
            return even_length_words
    except FileNotFoundError:
        return []

print(even_length_str("doc.txt"))

if __name__ == "__main__":
    file_path = "doc.txt"