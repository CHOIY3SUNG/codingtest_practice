a = input("입력 >>> ")

for i in range(len(a)):
    if a[i] != " ":
        if i % 2 == 0:
            print(a[i].upper(), end="")
        else:
            print(a[i], end="")
    else:
        print(" ", end="")