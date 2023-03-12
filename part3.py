from datetime import date
import datetime

age = 0 
pocket_money = 0
children_list = []

def calculate_age(dateOfBirth):
    current_date = date.today().strftime("%d-%m-%Y")
    the_age = current_date.year - dateOfBirth.year - ((current_date.month, current_date.day) < (dateOfBirth.month, dateOfBirth.day))
    return the_age

while (age != -1):
    name = (input("What is the child's name?\n"))
    date_of_birth = (input("What is the child's date of birth?\n"))
    dob = datetime.date(date_of_birth)
    age = calculate_age(dob)
   
    if (age < 5):
        pocket_money = 0
        child = (name, age, pocket_money)
        children_list.append(child)
    elif (age >= 5 or age <= 6):
        pocket_money = 5
        child = (name, age, pocket_money)
        children_list.append(child)
    elif (age >= 7 or age <= 9):
        pocket_money = 10
        child = (name, age, pocket_money)
        children_list.append(child)
    elif (age >= 10 or age <= 13 ):
        pocket_money = 20
        child = (name, age, pocket_money)
        children_list.append(child)
    elif (age >= 14 ):
        pocket_money = 30
        child = (name, age, pocket_money)
        children_list.append(child)
    else:
        break
print(children_list)









