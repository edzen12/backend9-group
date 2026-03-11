# Дан список чисел:
nums = [4, 7, 10, 15, 20, 23,17,7,12, 30]
# 1) С помощью цикла while пройти по списку.
n = 0 
while n < len(nums):
    print(nums[n])
    n += 1
# # 2) Выводить только нечётные числа.
n = 0 
while n < len(nums):
    if nums[n] % 2 != 0:
        print(nums[n])
    n += 1
# 3) Если встретилось число 20 — цикл должен остановиться. исп. break
n = 0 
while n < len(nums):
    if nums[n] == 20:
        break
    print(nums[n]) 
    n += 1
# 4) Все выведенные нечётные числа сохранить в множество odd_numbers.
setBlock = []
n = 0 
while n < len(nums):
    if nums[n] % 2 != 0:
        setBlock.append(nums[n])
    n += 1
setBlock = set(setBlock)
print(setBlock)