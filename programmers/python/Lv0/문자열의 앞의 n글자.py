# my_string = "ProgrammerS123"
# n = 11
my_string = "He110W0r1d"
n = 5

def solution(my_string, n):
    answer = ''
    for i in my_string:
        if len(answer) != n:
            answer += i
    return answer

print(solution(my_string, n))