# введем три переменные для нашего квадратного уравнения
a = int(input())
b = int(input())
c = int(input())
# напишем формулу дискримината для квадратного уравнения
d = b * b - 4 * a * c
# если дискриминат меньше нуля, то корней нет
if d < 0:
    print('')
# если дискриминат равен нулю,то у нас один корень
elif d == 0:
    print(-b/2*a)  # пишим формулу для нахождения корня
# если больше нуля , то у нас два корня, и пишим формулу из математики для нахождения х1 и х2
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(x1, x2)


