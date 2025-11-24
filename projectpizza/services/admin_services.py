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
def update_value():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT valor FROM produtos")
        conn.commit()
        value = cursor.fetchall()
        print(f"1 - Pizza de frango R${value[0]}\n2 - Pizza de camarão R${value[1]}\n3 - Pizza de calabresa R${value[2]}\n4 - Coca-cola R${value[3]}\n5 - Água s/gás R${value[4]}")
        id_product = int(input("Digite o id do produto: "))
        new_value = float(input("Digite o novo valor: "))
        cursor.execute("UPDATE produtos SET valor = %s WHERE produto_id=%s", (new_value, id_product))  
        conn.commit()
        print(f"Valor alterado para R$ {new_value}")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
    