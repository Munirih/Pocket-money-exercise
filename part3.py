from datetime import date

age = 0 
pocket_money = 0
children_list =[]

def calculate_age(dateOfBirth):
    current_date = date.today().strftime("%d-%m-%Y")
    the_age = current_date.year - dateOfBirth.year - ((current_date.month, current_date.day) < (dateOfBirth.month, dateOfBirth.day))
    return the_age

while (age != -1):
    name = (input("What is the child's name?\n"))
    date_of_birth = int(input("What is the child's date of birth?\n"))
    date_of_birth = date(date_of_birth).strftime("%d-%m-%Y")
    age = calculate_age(date_of_birth)
   
    if (age < 5):
        child = (name, age, pocket_money)
        children_list.append(child)
    elif (age == 5 or age == 6):
        pocket_money = 5
        child = (name, age, pocket_money)
        children_list.append(child)
    elif (age == 7 or age <= 9):
            pocket_money = 10
            child = (name, age, pocket_money)
            children_list.append(child)
    elif (age == 10 or age <= 13 ):
        pocket_money = 20
        child = (name, age, pocket_money)
        children_list.append(child)
    elif (age >= 14 ):
        pocket_money = 30
        child = (name, age, pocket_money)
        children_list.append(child)
print(children_list)









