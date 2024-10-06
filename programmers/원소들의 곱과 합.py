num_list = [3, 4, 5, 2, 1]


def solution(num_list):
    total = 0
    for number in num_list:
        total += number
        answer = total * total

    product = 1
    for number in num_list:
        product *= number

    if answer > product:
        return 1
    else:
        return 0


print(solution(num_list))
