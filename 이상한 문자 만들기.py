def solution(s):
    answer = ""
    count = 0
    for i in s:
        if i == " ":
            answer += " "
            count = 0
        elif count % 2 == 0:
            answer += i.upper()
            count += 1
        else:
            answer += i.lower()
            count += 1
    return answer