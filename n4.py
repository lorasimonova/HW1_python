# введем переменные
x = int(input())
a, b, c = int(), int(), int()
# первым этапом надо понять какие разряды присутствуют в данном числе и узнать их значение
if x // 100 > 0:
    a = x // 100
if (x % 100) // 10 > 0:
    b = x % 100 // 10
if 0 < x % 100 % 10 < 10:
    c = x % 100 % 10
# введем обозначения римских чисел и цифр
hundred = 'C'
fifty = 'L'
ten = 'X'
five = 'V'
one = 'I'
# дальше чтоб было проще в разрядах, я решила ввести такую переменную,чтобы она была равна римской сотне
sotnya = hundred
# дальше переведем десяток в римскую систему счисления
desyatok = str()
if 5 <= b < 9:
    desyatok = (fifty + (b - 5) * ten)
elif b == 9:
    desyatok = ten + hundred
elif b == 4:
    desyatok = ten + fifty
elif 1 <= b <= 3:
    desyatok = b * ten
# затем переведем единицу из арабской системы счисления в римскую,
# перевод практически аналогичный, что и в десятке
edinica = str()
if 5 <= c < 9:
    edinica = (five + (c - 5) * one)
elif c == 9:
    edinica = one + ten
elif c == 4:
    edinica = one + five
elif 1 <= c <= 3:
    edinica = c * one
# остается понять была ли сотня в разряде, и если да,
# то вывести ответ вместе с ней, иначе - без нее
if a:
    print(sotnya + desyatok + edinica)
else:
    print(desyatok + edinica)
