num1 = int(input("Please input the begin number: "))
num2 = int(input("Please input the end number: "))
for i in range(num1, num2 + 1):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)