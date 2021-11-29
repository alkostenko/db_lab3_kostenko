import psycopg2
from matplotlib import pyplot as plt

USERNAME='kostenko'
PASSWORD='1234'
DATABASE='coffe_and_code'
HOST='localhost'
PORT='5432'


query1='''
create view ProgrammerFavoriteCoffee as 
select trim(coffee.coffee_type), count(coder.coffee_id) 
from coffee inner join coder on coffee.id=coder.coffee_id
group by coffee.coffee_type
'''

query2='''
create view BugsSolve as
select trim(bugs.solve_bugs), count(coffee.id)
from bugs inner join coffee on bugs.id=coffee.id where coffee.coffee_type in ('Americano') 
group by bugs.solve_bugs;
'''

query3='''
create view CoffeeCupsPerDay as
select coffee.cups_per_day, count(coder.coffee_id) 
from coffee inner join coder on coffee.id=coder.coffee_id 
group by coffee.cups_per_day order by coffee.cups_per_day
'''

connection=psycopg2.connect(user=USERNAME, password=PASSWORD, dbname=DATABASE, host=HOST, port=PORT)

with connection:
    cursor = connection.cursor()

    colors=["#BEBDBF", "#D98E32", "#593622"]

    cursor.execute('drop view if exists ProgrammerFavoriteCoffee')
    cursor.execute(query1)
    cursor.execute('select * from ProgrammerFavoriteCoffee')

    data={}
    for row in cursor:
        data[row[0]]=row[1]
        print(row)
    
    plt.bar(list(map(lambda x: str(x), list(data.keys()))), data.values(), color=colors)
    plt.title("Програмісти, що пьють каву")
    plt.xlabel("Кількість програмістів")
    plt.ylabel("Назва кави")
    plt.show()


    cursor.execute('drop view if exists BugsSolve')
    cursor.execute(query2)
    cursor.execute('select * from BugsSolve')
    data={}
    for row in cursor:
        data[row[0]]=row[1]
        print(row)
        
    figure, ax=plt.subplots()  
    
    ax.pie(data.values(), labels=data.keys(), colors=colors)
    plt.title("Частка вирішених помилок у коді у тих, хто пье американо")
    plt.show()


    cursor.execute('drop view if exists CoffeeCupsPerDay')
    cursor.execute(query3)
    cursor.execute('select * from CoffeeCupsPerDay')
    data={}
    for row in cursor:
        data[row[0]]=row[1]
        print(row)
    
    plt.bar(list(map(lambda x: str(x), list(data.keys()))), data.values(), color=colors)
    plt.title("Кількість чашок кави на день")
    plt.xlabel("Кількість програмістів")
    plt.ylabel("Кількість чашок кави на день")
    plt.show()
