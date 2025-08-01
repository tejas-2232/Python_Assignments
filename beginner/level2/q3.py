'''
 Given an array of N integers and an integer K, find the number of
pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6
Sample Output: Pair count: 2
'''

def main():
    # Get array input and convert to list of integers
    arr_input = input("Enter the array elements separated by spaces: ")
    arr = list(map(int, arr_input.split()))
    k = int(input("Enter target sum k: "))
    
    count = 0
    
    # Method 1: Simple nested loop approach
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1
    
    print(f"Pair count: {count}")
    
if __name__ == "__main__":
    main()