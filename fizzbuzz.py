def fizzbuzz(num):
    # Melakukan perulangan

    for index in range(num):
        # Jika habis dibagi 3 dan 5 (modulo)
        # Tampilkan FizzBuzz

        if (index + 1) % 3 == 0 and (index + 1) % 5 == 0:
            print("FizzBuzz")

        # Tampilkan Fizz
        elif (index + 1) % 3 == 0:
            print("Fizz")

        # Tampilkan Buzz
        elif (index + 1) % 5 == 0:
            print("Buzz")

        # Return nilai angka
        else:
            print(index + 1)


fizzbuzz(20)
