from config.bd import create_connection
def ask_food(garcom_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedidos(garcom_id) VALUES (%s) RETURNING pedido_id", (garcom_id,))
        pedido_id = cursor.fetchone()[0]
        conn.commit()
        while True:    
            print("1 - Pizza de frango R$22.99\n2 - Pizza de camarão R$30.00\n3 - Pizza de calabresaR$20.00")
            produto_id = int(input("Digite um número para escolher: "))
            quantd = int(input("Digite quantos quer: "))
            cursor.execute("INSERT INTO pedido_produto(pedido_id, produto_id, quantidade) VALUES (%s, %s, %s)", (pedido_id, produto_id, quantd))
            conn.commit()
            resp = input("Deseja mais algo? (s/n)").lower()
            if resp == 's':
                continue
            elif resp == 'n':
                break
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
def list_food(id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT p.garcom_id, pp.pedido_id, pr.valor, pr.nome, pp.quantidade FROM  pedido_produto pp INNER JOIN produtos pr ON pp.produto_id=pr.produto_id INNER JOIN pedidos p ON pp.pedido_id=p.pedido_id WHERE pp.pedido_id = %s", (id,))
        conn.commit()
        lists = cursor.fetchall()
        return lists 
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
    