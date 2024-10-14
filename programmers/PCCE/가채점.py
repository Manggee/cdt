numbers = [3, 4]
our_score = [85, 93]
score_list = [85, 92, 38, 93, 48, 85, 92, 56]


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[i]:
            answer.append("Same")
        else:
            answer.append("Different")

    return answer


print(solution((numbers, our_score, score_list)))
