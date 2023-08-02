def fact_recursive(num):
    # Melakukan rekursif untuk mendapatkan faktorial
    # Jika num adalah 1, maka return 1

    if num <= 1:
        return 1

    # Return fungsi itu sekali lagi (recursive)
    # Kurangi parameternya
    else:
        # 3 * 2 * 1

        return num * fact_recursive(num - 1)


print(fact_recursive(5))
