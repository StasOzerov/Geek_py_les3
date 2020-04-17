
# p 5 ------------------------------------------------------------------

# first variant with function defined

def my_func(li):
    try:
        li = list(map(float, li))
        rezult = sum(li)
    except ValueError:
        print("Некорректные данные!")
        rezult = 0
    return rezult

print("Специальный символ 'q'")
rezult = 0
while True:
    a = input("Введите произвольное количество чисел через пробел:\n")
    li = a.split()
    if 'q' in li:
        i=li.index('q')
        li = li[:i]
        rezult += my_func(li)
        print("Конечная сумма =", rezult)
        print("Выход из программы.")
        break
    rezult += my_func(li)
    print("Конечная сумма =", rezult)


# # second variant without function defined
#
# print("Специальный символ 'q'")
# rezult = 0
# while True:
#     a = input("Введите произвольное количество чисел через пробел:\n")
#     li = a.split()
#     if 'q' in li:
#         i=li.index('q')
#         li = li[:i]
#         try:
#             li = list(map(float, li))
#             rezult += sum(li)
#             print(rezult)
#         except ValueError:
#             print("Некорректные данные!")
#             print(rezult)
#         print("Выход из программы.")
#         break
#     try:
#         li = list(map(float, li))
#         rezult += sum(li)
#         print(rezult)
#     except ValueError:
#         print("Некорректные данные!")
#         print(rezult)
