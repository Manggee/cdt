n = 0
control = "wsdawsdassw"


def solution(n, control):
    answer = 0
    for i in range(len(control)):
        if control[i] == "w":
            answer += 1
        elif control[i] == "s":
            answer -= 1
        elif control[i] == "d":
            answer += 10
        elif control[i] == "a":
            answer -= 10
    return n + answer

print(solution(n, control))