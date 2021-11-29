import json
import psycopg2

USERNAME='kostenko'
PASSWORD='1234'
DATABASE='coffe_and_code'
HOST='localhost'
PORT='5432'

OUTPUT='kostenko_DB.json'

TABLES=[
    'bugs',
    'coder',
    'coffee'
]

conn = psycopg2.connect(user=USERNAME, password=PASSWORD, dbname=DATABASE)

data={}
with conn:
    cur=conn.cursor()
    for table in TABLES:
        cur.execute('select*from '+table)
        rows=[]
        fields=[x[0] for x in cur.description]
        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table]=rows
    
with open(OUTPUT, 'w')as file:
    json.dump(data, file, default=str)