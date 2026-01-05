# 정수 배열 arr -> [0,1,2,3,4]
# 예) quries = [0,1] -> arr의 1번째와 2번째에 1씩 더하기

arr = [0, 1, 2, 3, 4]
queries = [[0, 1], [1, 2], [2, 3]]


def solution(arr, queries):
    for i in range(len(queries)):
        s, e = queries[i] # 쿼리에서 숫자 추출
        for j in range(s, e + 1):  # s ≤ j ≤ e 범위 처리
            arr[j] += 1
    return arr
print(solution(arr, queries))