age = 0 
pocket_money = 0
children_list =[]


while (age != -1):
    name = (input("What is the child's name?\n"))
    age = int(input("What's the child's age?\n"))
    if (age < 5):
        child = (name, pocket_money)
        children_list.append(child)
    elif (age == 5 or age == 6):
        pocket_money = 5
        child = (name, pocket_money)
        children_list.append(child)
    elif (age == 7 or age <= 9):
         pocket_money = 10
         child = (name, pocket_money)
         children_list.append(child)
    elif (age == 10 or age <= 13 ):
        pocket_money = 20
        child = (name, pocket_money)
        children_list.append(child)
    elif (age >= 14 ):
        pocket_money = 30
        child = (name, pocket_money)
        children_list.append(child)
print(children_list)