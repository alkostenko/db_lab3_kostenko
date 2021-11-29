import csv 
import decimal
import psycopg2

USERNAME='kostenko'
PASSWORD='1234'
DATABASE='coffe_and_code'
HOST='localhost'
PORT='5432'

INPUT='coffee.csv'

query_0 = '''
CREATE TABLE IF NOT EXISTS public.coffee_copy
(
    id int not null,
	cups_per_day int not null,
	coffee_type char(50)not null,
    constraint pk_coffee primary key(id)
)
'''

query_1 = '''
DELETE FROM coffee_copy
'''

query_2 = '''
INSERT INTO coffee_copy (id, cups_per_day, coffee_type) VALUES (%s, %s, %s, %s)
'''

conn = psycopg2.connect(user=USERNAME, password=PASSWORD, dbname=DATABASE)

with conn:
    cur = conn.cursor()
    cur.execute('drop table if exists coffee_copy')
    cur.execute(query_0)
    cur.execute(query_1)
    with open(INPUT, 'r') as inf:
        reader = csv.DictReader(inf)
        
        for idx, row in enumerate(reader):
            values = (row['Coffee_Id'], row["Cups_Per_Day"], row['Coffee_Type']) 
            cur.execute(query_2, values)

    conn.commit()