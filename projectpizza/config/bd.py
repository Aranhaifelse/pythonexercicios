import psycopg2
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname='auladb1',
            user='postgres',
            password='@Cat2000',
            host='localhost',
            port='5432'
        )
    except Exception as e:
        print(e)

