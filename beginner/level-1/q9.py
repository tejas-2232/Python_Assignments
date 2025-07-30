def main():
    # Ask user to enter the list
    user_list = input("Enter the list of numbers (comma-separated): ")
    # Convert the input string to a list of integers
    nlist = [int(x.strip()) for x in user_list.split(',')]
    
    # counting frequency of each element
    frequency = {}
    for num in nlist:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # print the frequency of each element
    print(f"Frequency count: {frequency}")
    
if __name__ == "__main__":
    main()
