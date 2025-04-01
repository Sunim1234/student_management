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
def create_tables():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(255) UNIQUE,
            enrollment_date DATE DEFAULT CURRENT_DATE
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created.")

def insert_data(name,age):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO student (std_id,first_name) VALUES(%s,%s) RETURNING id",(name,age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted.")
