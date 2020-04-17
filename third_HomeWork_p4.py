
# p 4 ------------------------------------------------------------------

while True:
    try:
        a = float(input("Введите действительное положительное число:\n"))
    except ValueError:
        print("НЕКОРРЕКТНЫЙ ВВОД! Всё по новой.")
        continue
    if a > 0:
        try:
            b = int(input("Введите целое отрицательное число:\n"))
        except ValueError:
            print("НЕКОРРЕКТНЫЙ ВВОД! Всё по новой.")
            continue
        if b < 0:
            break
        else:
            print("НЕКОРРЕКТНЫЙ ВВОД! Всё по новой.")
            continue
    else:
        print("НЕКОРРЕКТНЫЙ ВВОД! Всё по новой.")
        continue

# first variant
def my_func1(x, y):
    return x**y

# second variant
def my_func2(x, y):
    i = -1
    tmp = x
    while i > y:
        tmp *= x
        i -= 1
    return 1 / tmp

# third variant
my_func3 = lambda x, y: x**y

print(a, "**", b, "=", my_func1(a, b))
print(a, "**", b, "=", my_func2(a, b))
print(a, "**", b, "=", my_func3(a, b))
