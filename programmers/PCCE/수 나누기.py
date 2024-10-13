number = 2000000000
answer = 0

# 명답..
for i in range(len(str(number)) // 2):
    answer += number % 100  # 나머지
    number //= 100  # 몫
print(answer)

# 나의 하찮은 정답
for i in range(5):
    answer += number % 100  # 나머지
    number //= 100  # 몫
print(answer)
