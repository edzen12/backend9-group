# 1
# 'hello', "hello 2", """hello 3"""

# 2
print('hello'*3) 

#3 
a = 45
b = 4.5
c = True
d = str(a)
print(type(d))
d = str(b)
print(type(d))
d = str(c)
print(type(d))

#4
# индексы - это нумерация строк, индексы начинаются с нуля используя квадратные скобки []
# срезы [start:stop:step]
name = 'Gena Krocodil and Cheburashka'
print(name[5:13]+name[18:])
print(name[4:]) # начинаем от 4го до конца
print(name[:13]) # начинаем от нуля до 13 
print(name[::3]) # от начала и до конца, только с шагом 2


# 5
text = """Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.
"""
print(len(text)) # общее количество букв: 983
print(text.count('s')) #62
print(text.count('t')) #71

#6
some_string = "Adverts"
print(some_string[1::2])
print(some_string[2:5])
print(some_string[2]+some_string[3]+some_string[4])

#7
name1 = 'Adilet'
name2 = 'Aidana'
print(name1[0]+name2[0]+name1[1]+name2[1]+name1[2]+name2[2]+name1[3]+name2[3]+name1[4]+name2[4]+name1[5]+name2[5])