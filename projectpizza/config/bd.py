import psycopg2
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname='projetopizza',
            user='postgres',
            password='123456',
            host='localhost',
            port='5432'
        )
        print("Conexão com Sucesso!")
        return conn
    except Exception as e:
        print(e)

