def count_customers(N,S):
    seen = set()
    active = set()
    walked_away = 0

    for c in S:
        if c not in seen:
            seen.add(c)
            if len(active) < N:
                #allocate a computer
                active.add(c)
            else:
                walked_away += 1
        else:
            #departure
            if c in active:
                active.remove(c)
    return walked_away


if __name__ == "__main__":
    print(count_customers(3, "GACCBDDBAGEE"))
    print(count_customers(1, "ABCBAC")) 