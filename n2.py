# введем 4 переменных
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# координаты должны быть отличными от нуля,если верно выводим yes
if x1 * y1 > 0 and x2 * y2 > 0:
    print("YES")
else: # иначе выводим no
    print("NO")
