genas = []
for i in range(101):
    genas.append(i)
print(genas)
############# генератор списков - List comprehension
nukes = [i for i in range(50)]
print(nukes)
#############
nukes2 = [i for i in range(51) if i % 2 !=0]
print(nukes2)
#############  Dict comprehension - генератор Словарей
marks = {
	'Mark': 40,
	'Agnes': 50,
	'Helen': 80,
	'John': 65,
}
new_marks = { k:v + 10 for k, v in marks.items() }
print(new_marks)
# №№№№№№№№№№№
students_with_class = { k+" A":v for k, v in new_marks.items() }
print(students_with_class)