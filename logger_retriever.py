import datetime

print("'''''''''''''''''''' Welcoe to Health Logger and Retiver System ''''''''''''''''''''")

op = input("Enter want do you want to do / L / 'log' or / R / 'retrive : ")
if(op == "L" or 'l'):
    name = input("Enter for whom you want to log '1' for - Harry '2' for Pratham : ")

    if(name == '1'):
        
        val = input("Enter what do you want to log (1) for - 'food' or (2) for - 'activity' : ")

        if(val == '1'):
            
            food_n = input("Enter food item : ")

            with open("Harry-food.txt",'a') as op:
                op.write(f"food item : {food_n} Time - {datetime.datetime.now()} \n")
                print("Item added successfully")
            
            
        elif(val == '2'):

            act_n = input("Enter activity name : ")

            with open("Harry-activity.txt",'a') as op:
                op.write(f"Activity : {act_n} Time - {datetime.datetime.now()} \n")
                print("Activity added successfully")
           
    elif(name == '2'):
        val = input("Enter what do you want to log (1) for - 'food' or (2) for - 'activity' : ")

        if(val == '1'):
            
            food_n = input("Enter food item : ")

            with open("Pratham-food.txt",'a') as op:
                op.write(f"food item : {food_n} Time - {datetime.datetime.now()} \n")
                print("Item added successfully")
            
            
        elif(val == '2'):

            act_n = input("Enter activity name : ")

            with open("Pratham-activity.txt",'a') as op:
                op.write(f"Activity : {act_n} Time - {datetime.datetime.now()} \n")
                print("Activity added successfully")
else:
    name = input("Enter of whom you want to retrive '1' for - Harry '2' for Pratham : ")
    if name == '1':
        val = input("Enter what to retive '1' for - Food-items or '2' for - Activities : ")

        if val == '1':

            with open('Harry-food.txt') as rd:
                for i in rd:
                    print(i)

        elif val == '2':

            with open('Harry-activity.txt') as rd:
                for i in rd:
                    print(i)

    elif name == '2':
        val = input("Enter what to retive '1' for - Food-items or '2' for - Activities : ")

        if val == '1':

            with open('Pratham-food.txt') as rd:
                for i in rd:
                    print(i)

        elif val == '2':

            with open('Pratham-activity.txt') as rd:
                for i in rd:
                    print(i)

    