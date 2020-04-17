
# p 2 ------------------------------------------------------------------

name = input("Введите имя:\n")
soname = input("Введите фамилию:\n")

while True:
    birth = input("Введите год рождения:\n")
    if birth.isdigit() == True:
        break
    else:
        print("Некорректный год рождения!")

city = input("Введите город проживания:\n")
email = input("Введите e-mail:\n")

while True:
    tel = input("Введите номер телефона:\n")
    if tel.isdigit() == True:
        break
    else:
        print("Некорректный номер телефона!")

def inform(**kwargs):
    return kwargs

a = inform(имя=name,
           фамилия=soname,
           год=birth,
           город=city,
           e_mail=email,
           телефон=tel,)
print(a)
