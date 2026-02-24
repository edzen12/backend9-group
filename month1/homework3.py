#1 "Gena Crocodil" "G.C."
fullName = input("Введите Имя и Фамилию: ")
out = fullName[0].upper()+'.'+fullName[5].upper()+'.'
print(out)

# №2
# [start:stop:step] 
fullName = input("Введите любое слово: ")
print(fullName[::-1])

#4
fullName = input("Введите любое слово: ")
chet_slov = len(fullName)-1 
print(f"Первый: {fullName[0]},  Последний: {fullName[chet_slov]}")
#5
name = ' Ахмед Давлетович '
name = name.replace(' ', '')
print(name)