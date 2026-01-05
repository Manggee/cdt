price = int(10000)
money = int(3000)

count = 0
account = 0

while account < price:
    count += 1
    account += money
    account += account * 5 // 100

print(count)

