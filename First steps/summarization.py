def summation(num):
    steps = '0'
    summa = 0
    for element in range(1, num + 1):
        print('for element: ' + str(element))
        steps += '+' + str(element)
        summa += element

    print('summa ' + str(summa))
    print('steps ' + steps)

summation(7)

