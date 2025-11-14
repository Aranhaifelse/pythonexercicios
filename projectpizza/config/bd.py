import psycopg2
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname='projetopizza',
            user='postgres',
            password='@Cat2000',
            host='localhost',
            port='5432'
        )
        print("Conexão com Sucesso!")
        return conn
    except Exception as e:
        print(e)

