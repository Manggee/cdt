arr1 = [49, 13]
arr2 = [70, 11, 2]

def solution(arr1, arr2):
    answer = 0
    if len(arr1) < len(arr2):
        return -1
    elif len(arr2) < len(arr1):
        return 1
    else:
        sum_arr1 = sum(arr1)
        sum_arr2 = sum(arr2)
        if sum_arr1 < sum_arr2:
            return -1
        elif sum_arr1 > sum_arr2:
            return 1
    return answer

print(solution(arr1, arr2))