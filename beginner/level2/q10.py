def generate_piles(n):
    
    piles = [] #empty list to store piles

    if n %2==1:
        start_value = 2
    else:
        start_value = 1

    current = start_value

    while current < n:
        piles.append(current)
        current += 2

    return piles


if __name__ == "__main__":
    n = int(input("enter number of piles to make::"))
    result = generate_piles(n)
    print("stones in each pile :", result)