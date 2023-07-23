def multiplication_table(num):
    for element in range(1, 11):
        result = num * element
        # print(str(num) + 'x' + str(element) + '=' + str(result))
        # print(num, 'x', element, '=', result)
        print(f"{num} x {element} = {result}")


multiplication_table(6)
