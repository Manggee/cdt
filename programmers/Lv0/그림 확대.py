picture = [".xx...xx.",
           "x..x.x..x",
           "x...x...x",
           ".x.....x.",
           "..x...x..",
           "...x.x...",
           "....x...."]
k = 2


def solution(picture, k):
    answer = []
    for i in picture:
        line = ""
        for j in i:
            line += (j * k)

        for _ in range(k):
            answer.append(line)
    return answer

print(solution(picture, k))


# 1) 한줄씩 읽어 각 글자를 k번 반복해서 가로 늘리기
# 2) 만들어진 한 줄을 k번 복사해서 세로 늘리기
# 3) 결과를 리스트에 담기