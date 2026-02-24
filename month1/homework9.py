# Spisok = [1,2,3,-4,5,6,7,-8,9,10,20,30,-40,-50,100]
# poloj_number = []
# otrisat_number = []
# for i in Spisok:
#     if i > 0:
#         poloj_number.append(i)
#     elif i < 0:
#         otrisat_number.append(i)

# print(f'только положительные числа: {poloj_number}')
# print(f'только отрицательные числа: {otrisat_number}')

# №№№№№№№ 2
# Spisok = [1,2,3,-4,5,6,7,-8,9,10,20,30,-40,-50,100]
# chet_number = []
# for num in Spisok:
#     if num % 2 == 0:
#         chet_number.append(num)

# print(chet_number)
# №№№№№№№ 3
# Spisok = [1,2,3,-4,5,6,7,-8,9,10,20,30,-40,-50,100]
# nums_after_ten = []
# for nums in Spisok:
#     if nums > 10:
#         nums_after_ten.append(nums)
# print(f"Чисел больше 10ти: {len(nums_after_ten)} штук")
# №№№№№№№№4
# Spisok = [1,2,3,-4,5,6,7,-8,9,103,7,20,30,-40,-50,100]
# nechet = []
# for i in Spisok:
#     if i % 2 !=0:
#         nechet.append(i)
# print(nechet)
# # способ №1
# print("сумма нечетных: ", sum(nechet)) 
# #### # способ №2
# n = 0
# for num in nechet:
#     n+=num
# print(f"сумма нечетных: {n}") 

#5
# Spisok = [1,2,3,-4,5,6,7,-8,9,103,7,20,30,-40,-50,100]
# for i in Spisok:
#     if i % 3 == 0:
#         print(i)

# цикл 
#     break - стоп
#     continue - продолжать
# Spisok = [1,2,3,-4,5,6,7,-8,9,0,7,20,30,-40,-50,100]
# останавливаем до 0
# for num in Spisok:
#     if num == 0:
#         break
#     print(num)
# # пропускаем 0 и показываем остальное
# for num in Spisok:
#     if num == 0:
#         continue
#     print(num)

#8
Spisok = [1,2,3,-4,5,6,7,-8,9,0,7,20,30,-40,-50,100]
kvadrat_chisel = []
for num in Spisok:
    if num > 0:
        kvadrat_chisel.append(num**2)
print(kvadrat_chisel)
# 9