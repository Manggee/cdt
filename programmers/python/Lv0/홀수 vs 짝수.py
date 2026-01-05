# 1번 풀이
def solution(num_list):
    even = 0
    odd = 0

    for i in range(0, len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]
    if even > odd:
        return even
    else:
        return odd


# 2번 풀이
def solution(num_list):
    even = sum(num_list[::2])
    odd = sum(num_list[1::2])
    return max(even, odd)

print(solution([4,2,6,1,7,6]))