def main():
    n = input("enter list of numbers:")
    n = n.split()
    n = [int(i) for i in n]
    n.sort()
    if len(n) % 2 == 0:   #if even
        mid  = len(n)//2
        median = (n[mid-1] + n[mid])/2
    else:   #if odd
        mid = len(n)//2
        median = n[mid]
    print(f"Median: {median}")

if __name__ == "__main__":
    main()