

# def fizz_buzz(input):
#     if input % 3 == 0:
#         result = "Fizz"
#     else:
#         result = "Buzz"
#     return result


# print(fizz_buzz(3))

# Es geht aber noch eleganter:

# def fizz_buzz(input):
#     if input % 3 == 0:
#          return = "Fizz"
#      else:
#          return = "Buzz"


# print(fizz_buzz(3))


# ooooder noch besser

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
