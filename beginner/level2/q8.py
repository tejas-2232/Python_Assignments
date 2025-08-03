def count_vowels(string):
    vowels = set("aeiouAEIOU")
    count = 0
    
    for char in string:
        if char in vowels:  # O(1) average lookup in set
            count += 1
    
    return count

def main():    
    user_string = input("Enter a string to count vowels: ")

    vowel_count = count_vowels(user_string)
    print(f"Number of vowels: {vowel_count}")

if __name__ == "__main__":
    main()