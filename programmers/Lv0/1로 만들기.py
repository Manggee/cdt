num_list = [12, 4, 15, 1, 14]

def solution(num_list):
    cnt = 0
    for i in num_list:
        while i != 1:
            if i % 2 == 0:
                i = i / 2
                cnt += 1
            elif i % 2 == 1:
                i = (i - 1) / 2
                cnt += 1
    return cnt

print(solution(num_list))