
# p 1 ------------------------------------------------------------------

# first variant

def my_div():
    while True:
        try:
            a = float(input("Введите числитель:\n"))
            b = float(input("Введите знаменатель:\n"))
        except ValueError:
            print("Значения введены НЕВЕРНО!")
            continue
        try:
            rezult = a / b
        except ZeroDivisionError:
            print("На 0 делить НЕЛЬЗЯ!")
            continue
        print("результат деления:", rezult)
        break

my_div()


# second variant

# while True:
#     try:
#         a = float(input("Введите числитель:\n"))
#         b = float(input("Введите знаменатель:\n"))
#     except ValueError:
#         print("Значения введены НЕВЕРНО!")
#         continue
#     break
#
# def my_div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("На 0 делить НЕЛЬЗЯ!")
#
# c = my_div(a, b)
# print(c)
