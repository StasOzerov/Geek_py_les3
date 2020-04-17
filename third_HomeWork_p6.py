
# p 6 ------------------------------------------------------------------

from re import search

def int_func(my_str):
    if my_str.islower() and my_str.isalpha() and bool(search('[а-яА-Я]', my_str)) == False:
        return my_str.capitalize()
    else:
        return None

u = input("Введите несколько слов на латинском языке\n"
          "(все буквы всех слов должны быть в нижнем регистре):\n")
li = u.split(' ')
len_li = len(li)

while len_li != 0:
    li[len_li-1] = int_func(li[len_li-1])
    len_li -= 1

for itm in li:
    if itm == None:
        li.remove(itm)

print(' '.join(li))
