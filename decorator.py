#problems1
# def glav():
#     a = 'Я главная функция'
#     print(a)
#     def vloj():
#         b = 'Я вложенная функция'
#         print(b)
#     vloj()
# glav()

#problems2
# a = {'1':4, '2':5, '3':6}
# def dict_kv(d):
#     b = tuple(d.keys())
#     c = tuple(d.values())
#     return b,c
# print(dict_kv(a))

#problems3
# num = int(input('Введите простое число: '))
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print('False')
#             break
#     else:
#         print('True')
# else:
#     print('False')

#problems4
# def decor(f):
#     def deleted():
#         l = f()
#         return list(set(l))
#     return deleted

# @decor

# def rando():
#     import random as rad
#     lst = []
#     for i in range(0,100):
#         random_number = rad.randint(10,50)
#         lst.append(random_number)
#     return lst

# print(rando())

# #problems5
# def shifr(f,*args):
#     def word_shifr(*args):
#         shifr_login=""
#         shifr_password=""
#         login,password = f(*args)
#         for i in login:
#             shifr_login+= str(ord(i))+"*"
#         for i in password:
#             shifr_password+= str(ord(i))+"*"
#             return shifr_login, shifr_password
#     return word_shifr

# @shifr
# def login(l,p):
#     return l, p
# l = input("login: ")
# p = input ("password: ")
# print(login(l,p))

#problems7
# def add(a,b):
#     return a + b

# def substract(a,b):
#     return a - b

# def multiply(a,b):
#     return a * b

# def divide(a,b):
#     return a / b
# print(add(2,5))
# print(substract(6,3))
# print(multiply(4,5))
# print(divide(9,3))