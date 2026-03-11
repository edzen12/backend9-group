# Есть два множества:
group_a = {"Aibek", "Nursultan", "Adilet", "Azamat"}
group_b = {"Adilet", "Azamat", "Ermek"}

while True:
    name = input("Введите имя: ")
    if name == 'stop':
        break
    if name in group_a and name in group_b:
        print("Студент состоит в двух группах") 
    elif name in group_a and name not in group_b:
        print("Студент состоит только в одной группе")
    elif name in group_b and name not in group_a:
        print("Студент состоит только в одной группе")
    elif name not in group_a and name not in group_b:
        print('Нет его в обоих группах')
    
     

