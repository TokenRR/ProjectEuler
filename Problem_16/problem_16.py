number = 2**1000
acc= 0
number_str = str(number)
for i in number_str:
    acc += int(i)
print(acc)