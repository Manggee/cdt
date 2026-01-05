num_list = [3, 4, 5, 2, 1]


def solution(num_list):
    answer_1 = ""
    answer_2 = ""
    for i in range(len(num_list)): # 0,1,2,3,4
        if num_list[i] % 2 == 0:
            answer_1 += str(num_list[i])
        else:
            answer_2 += str(num_list[i])
    answer = int(answer_1) + int(answer_2)
    return answer
print(solution(num_list))


