
# p 3 ------------------------------------------------------------------

# first variant
def my_sum(a:float,b:float,c:float):
    li = [a,b,c]
    li.sort()
    return li[1] + li[2]

# second variant
def my_sum2(*args):
    li = [*args]
    li.sort()
    try:
        return li[-2] + li[-1]
    except IndexError:
        print("Длина кортежа меньше двух элементов! НЕДОПУСТИМО!")

while True:
    try:
        a = float(input("Введите число a:\n"))
        b = float(input("Введите число b:\n"))
        c = float(input("Введите число c:\n"))
    except ValueError:
        print("Значения введены НЕКОРРЕКТНО!")
        continue
    break

k = my_sum(a, b, c)
print(k)

k = my_sum2(a, b, c)
print(k)
