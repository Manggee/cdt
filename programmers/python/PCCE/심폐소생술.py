cpr = ["call", "respiration", "repeat", "check", "pressure"]


def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(0, len(basic_order)):
            if action == basic_order[i]:
                answer.append(i + 1)
    return answer


print(solution(cpr))

# cpr배열에 대해 for loop를 수행하며 basic_order에서 몇 번째인지의 index값을 찾은 뒤 answer에 index+1값을 저장합니다.
