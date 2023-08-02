def factorial(num):
    # Nilai awal

    result = 1

    # Melakukan perulangan untuk menghitung hasil faktorial
    # Contoh: num = 5
    # Maka: 1 * 2 * 3 * 4 * 5

    for i in range(1, num + 1):
        result *= i

    # Return hasil

    return result


print(factorial(5))
