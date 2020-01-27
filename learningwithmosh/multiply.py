def mulitply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(mulitply(1, 2, 3))
print("finish")
