'''
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
Sample Output: list2 = [1, 2, 3, 4, 5]
'''

def unique_elements(l):
    l1 = []
    for item in l:
        if item not in l1:
            l1.append(item)
    return l1

def main():
    l = input("Enter the list of numbers separated by space:")
    l = l.split()
    l = [int(i) for i in l]
    unique_list = unique_elements(l)
    print(f"Unique elements: {unique_list}")

if __name__ == "__main__":
    main()