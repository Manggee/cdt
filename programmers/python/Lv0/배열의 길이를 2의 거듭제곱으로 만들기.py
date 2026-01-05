arr = [1, 2, 3, 4, 5, 6]

def solution(arr):
    answer = [2**i for i in range(11)]
    while len(arr) not in answer:
        arr.append(0)
    return arr
print(solution(arr))

# arr의 길이가 2의 거듭제곱이 되어야함
# 최소한으로 0 붙이기

# 2의 거듭제곱 목록을 생성
# 배열 길이가 2의 거듭제곱인지 확인한 후 아니면 0 붙이기
# while로 계속 반복
