num_list = [5, 2, 1, 7, 5]

def solution(num_list):
    if num_list[-1] > num_list[-2]:
        new1_num = num_list[-1] - num_list[-2]
        num_list.append(new1_num)

    else:
        new2_num = num_list[-1] * 2
        num_list.append(new2_num)

    return num_list

print(solution(num_list))


# 마지막 원소와 그 전 원소 크기 비교
# 경우의 수 1: 마지막 원소 < 이전 원소
# 마지막 원소 * 2 -> 리스트에 추가
# 경우의 수 2: 이전 원소 < 마지막 원소
# 마지막 원소 - 이전 원소 -> 리스트에 추가

# 생각하지 못한 부분:
# '크지 않다' 라는 말은 두 수가 같은 경우에도 해당이 된다. 이 부분을 생각하지 못했다.


