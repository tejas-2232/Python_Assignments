def main():
    input_list = input("Enter list of strings: ").split()
    
    # Convert each string to list of characters using MAP function
    indv = list(map(list, input_list))
    print(f"Characters list: {indv}")

if __name__ == "__main__":
    main()