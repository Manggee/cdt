myString = "oxooxoxxox"
def solution(myString):
    answer = []
    a = myString.split('x')
    for i in a:
        answer.append(len(i))
    return answer

print(solution(myString))