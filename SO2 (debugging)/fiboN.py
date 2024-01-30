def fibon(n):
    list = []
    for i in range(0, n):
        if i == 0 or i == 1:
            list.append(i)
        else:
            before2 = list[i - 2]
            before1 = list[i - 1]
            list.append(before1 + before2)
    print(list[-1])

print(f"this is the 5th term: {fibon(5)}.")
