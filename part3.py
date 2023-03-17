from datetime import datetime

children = [('John', '2018-03-05'), ('Jane', '2007-09-09'), ('Jennifer', '2011-01-01')]
children_list = []
child = ()
def calculate_age(dateOfBirth):
    dateOfBirth = datetime.strptime(dateOfBirth, "%Y-%m-%d").date()
    current_date = datetime.date(datetime.now())
    the_age = current_date.year - dateOfBirth.year - ((current_date.month, current_date.day) < (dateOfBirth.month, dateOfBirth.day))
    return the_age



for index, item in enumerate(children):
    child = children[index]
    name = child[0]
    date_of_birth = child[1]

    age = calculate_age(date_of_birth)

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
print(children_list)
