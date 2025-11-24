from config.bd import create_connection
from config.crypt import checar_password,criotpgrafer
def insert_user(email: str, password: str, name: str, fone: str):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        password = criotpgrafer(password)
        cursor.execute("INSERT INTO garcons (email, password, nome, telefone) VALUES (%s, %s, %s, %s)", (email, password, name, fone))
        conn.commit()
        print("Garçom cadastrado!")
    except Exception as e:
        print(e)
    
        

def login(email: str,password: str):
    try:
        conn = create_connection()
        cursor = conn.cursor() #Cursor() Manda e recebe os comandos entre o python e o Banco de dados
       
        cursor.execute("SELECT * FROM garcons WHERE email=%s", (email,)) 
        conn.commit()
        user = cursor.fetchone()
        if user and checar_password(password, bytes(user[4])):
            return user  
        return None
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()