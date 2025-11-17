from config.bd import create_connection
def insert_product(valor, nome):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO produtos(valor, nome) VALUES (%s, %s)", (valor, nome))
        conn.commit()
        print("Produto cadastrado!")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
def update_value(id_product, new_value):
    try:

        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE produtos SET valor = %f WHERE produto_id=%d", [new_value, id_product])  
        conn.commit()
        print(f"Valor alterado para R$ {new_value}")
    except Exception as e:
        print(e)
    finally:
        conn.close()

    