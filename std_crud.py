
import psycopg2

# connection to datbase and eexception handling
def db_connection():
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres.xodjwyowgwlrlkkunjuf", password="EisRhFQyrmBOvF9n",host="aws-0-ap-southeast-1.pooler.supabase.com",port="5432")
        print(conn)
        return conn
    except Exception as e:
        print("Error connecting to database.")
        return None
'''def create_tables():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL)
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created.")

def insert_data(name,age):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO teacher (name,age) VALUES(%s,%s) RETURNING id",(name,age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted.")'''

'''def upd_data(a):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE teacher SET age=56 WHERE age = '%s'",(a,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data updated.")

def del_data(a):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM teacher WHERE age = '%s'",(a,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data deleted.")'''

def show_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher;")
    results = cursor.fetchall()
    print('(id, name, age, course_id, department_id)')
    for row in results:
        print (row)
    conn.commit()
    cursor.close()

# int/ void main equivalent
if __name__ == "__main__":
    '''create_tables()
    insert_data("Ram",21)
    upd_data(21);
    del_data(21)'''
    show_table()