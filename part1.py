age = 10


if (age < 5):
    pocket_money = 0
elif (age >= 5 or age <= 6):
    pocket_money = 5
elif (age == 7 or age <= 9):
    pocket_money = 10   
elif (age == 10 or age <= 13 ):
    pocket_money = 20   
elif (age >= 14 ):
    pocket_money = 30
    
    
print (f'The pocket money is R{pocket_money}')