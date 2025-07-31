def main():
    #accept 2 input lists from user l1 and l2
    l1 = input("Enter the list of numbers:")
    l2 = input("Enter the list of numbers:")

    set1 = set(l1)
    set2 = set(l2)

    #find common in both sets
    common = set1 & set2
    # return as a list
    common_list = list(common)

    print(f"Common elements: {common_list}")


if __name__ == "__main__":
    main()