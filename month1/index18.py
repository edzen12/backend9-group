# Функции
#     встроенные
        
#     пользовательские
#         def 
#         lambda

def twosum(a,b):
    return a+b
print(twosum(5,8))

# lambda функции - анонимные функции - функции без имени
res = lambda x, y: x*y
print(res(5,6))
########  
print((lambda a,b:a/b)(int(input("первое число: ")), int(input("второе число: "))))
