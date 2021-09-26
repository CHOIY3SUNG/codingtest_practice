def nandx(n):
    for x in range(n+1):
        if x*x == n:
            return (x+1) * (x+1)
    return -1
a = int(input())
print(nandx(a))