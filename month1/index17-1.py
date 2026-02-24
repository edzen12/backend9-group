# модуль
import random 
import datetime

res = random.randint(1, 9)
print("рандомное число: ", res)
######
time = datetime.datetime.today() 
print(time)

try:
    print(10/2)
except ZeroDivisionError:
    print("На ноль я случайно поделил, я не дурак")