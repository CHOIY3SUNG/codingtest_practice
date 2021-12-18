def solution(arr):
    def gcd(x, y):
        while y:
            x,y = y, x%y
        return x
    def lcd(x, y):
        return x * y // gcd(x, y)
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcd(answer, arr[i])
    return answer

print(solution([2,6,8,14])) #test
