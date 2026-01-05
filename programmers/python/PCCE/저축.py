# start = int(input())
# before = int(input())
# after = int(input())
start = 28
before = 6
after = 8

money = start
month = 1
while money < 70:
    money += start
    month += 1
while money < 100:
    money += after
    month += 1
print(month)
