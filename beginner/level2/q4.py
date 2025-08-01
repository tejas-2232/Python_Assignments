'''Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
'''

def main():
    n = input("Enter the array: ")
    n = n.split()
    n = [int(i) for i in n]
    d = int(input("Enter the number of elements to rotate by (D): "))
    
    # edge case
    if len(n) == 0:
        print("Array is empty")
        return
    
    # Optimize D - avoids unnecesary full rotations
    d = d % len(n)
    
    if d == 0:
        print(f"Arr after rotation: {n}")
        return    
    # Rotate array using slicing
    rotated_array = n[-d:] + n[:-d]

    print("Arr after rotation:",rotated_array)

if __name__ == "__main__":
    main()