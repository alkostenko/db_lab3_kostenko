import csv
import psycopg2

USERNAME='kostenko'
PASSWORD='1234'
DATABASE='coffe_and_code'
HOST='localhost'
PORT='5432'

OUTPUT='kostenko_DB{}.csv'

TABLES=[
    'bugs',
    'coder',
    'coffee'
]

conn = psycopg2.connect(user=USERNAME, password=PASSWORD, dbname=DATABASE)

with conn:
    cur=conn.cursor()

    for table in TABLES:
        cur.execute('select*from '+table)
        fields=[x[0] for x in cur.description]

        with open(OUTPUT.format(table), 'w')as outfile:
            writer=csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x).lstrip()for x in row])
