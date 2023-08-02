def fact_recursive(num):
    if num <= 1:
        return 1
    else:
        # 3 * 2 * 1

        return num * fact_recursive(num - 1)


print(fact_recursive(3))
