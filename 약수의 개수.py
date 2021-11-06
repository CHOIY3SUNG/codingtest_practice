# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            count = 0
            for l in range(1,j):
                if j % l == 0:
                    count += 1
        if count % 2 == 0:
            answer -= i
        else:
            answer += i
    return answer
#   return sum([-n if int(n ** 0.5) == n ** 0.5 else n for n in range(left, right+1)])

print(solution(13, 17))