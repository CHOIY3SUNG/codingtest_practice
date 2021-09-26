def bs(n):
    n = list(map(int, n))
    n.sort(reverse=True)
    ret = ""
    for i in range(len(n)):
        ret += str(n[i])
    return ret

n = list(input("입력 : "))
print(bs(n))