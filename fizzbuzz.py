def fizzbuzz(num):
    for index in range(num):
        if (index + 1) % 3 == 0 and (index + 1) % 5 == 0:
            print("FizzBuzz")
        elif (index + 1) % 3 == 0:
            print("Fizz")
        elif (index + 1) % 5 == 0:
            print("Buzz")
        else:
            print(index + 1)


fizzbuzz(20)
