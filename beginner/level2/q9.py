def access_list_element(lst, index):
    try:
        element = lst[index]
        print(f"Element at index {index}: {element}")
        return element
    except IndexError:
        print(f"IndexError: Index {index} is out of range for list of length {len(lst)}")
        return None

def main():
    
    my_list = [10, 20, 30, 40, 50]
    print(f"List: {my_list}")
    print(f"Valid indices: 0 to {len(my_list)-1}")
    print("-" * 40)
    
    # Test different index
    test_indices = [0, 2, 5, -1, 10]
    
    for index in test_indices:
        access_list_element(my_list, index)
        print()

if __name__ == "__main__":
    main()