#create an empty tuple and an empty list 
child = ()
children_list =[]
#given the list of children with their names and age 
children = [('John', 5), ('Mary', 15)] 

#loop through the list to access the name and age of a child
for index, item in enumerate(children):
    child = children[index]
    name = child[0]
    age = child[1]

    if (age < 5):
        pocket_money = 0
        #store the name and pocket money of a child in a tuple
        c = (name, pocket_money) 
        #add the tuple into a list
        children_list.append(c) 
    elif (age == 5 or age <= 6):
        pocket_money = 5
        c = (name, pocket_money)
        children_list.append(c)
    elif (age == 7 or age <= 9):
         pocket_money = 10
         c = (name, pocket_money)
         children_list.append(c)
    elif (age == 10 or age <= 13):
        pocket_money = 20
        c = (name, pocket_money)
        children_list.append(c)
    elif (age >= 14 ):
        pocket_money = 30
        c = (name, pocket_money)
        children_list.append(c)

#print all the tuples in a list
print(children_list)
