# введем две переменные a и b
a = int(input())
b = int(input())
# если а и b равны нулю ,то решений нет
if (a == 0 and b == 0):
    print('INF')
# если a равно нулю а при делении b на а остаток не равен нулю, то решение конечно
elif (a == 0 or (b % a) != 0):
    print('NO')
# чтоб решить уравнение мы должны -b поделить на а , выведим
else:
    print(int(-b / a))

