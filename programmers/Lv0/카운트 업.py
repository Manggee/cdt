start_num = 3
end_num = 10

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer
print(solution(start_num, end_num))