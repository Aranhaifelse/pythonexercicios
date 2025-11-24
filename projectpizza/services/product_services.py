from config.bd import create_connection
def ask_food(garcom_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedidos(garcom_id) VALUES (%s) RETURNING pedido_id", (garcom_id,))
        conn.commit()
        pedido_id = cursor.fetchone()[0]
        pessoas = int(input("Digite quantas pessoas tem na mesa: "))
        cursor.execute("INSERT INTO mesas(pessoas, pedido_id) VALUES (%s, %s)", (pessoas, pedido_id))
        conn.commit()
        while True:    
            cursor.execute("SELECT valor FROM produtos")
            value = cursor.fetchall()
            print(f"1 - Pizza de frango R${value[0]}\n2 - Pizza de camarão R${value[1]}\n3 - Pizza de calabresa R${value[2]}\n4 - Coca-cola R${value[3]}\n5 - Água s/gás R${value[4]}")
            produto_id = int(input("Digite um número para escolher: "))
            quantity = int(input("Digite quantos quer: "))

            cursor.execute("INSERT INTO pedido_produto(pedido_id, produto_id, quantidade) VALUES (%s, %s, %s)", (pedido_id, produto_id, quantity))
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
        cursor.execute("SELECT m.mesa_id, m.pessoas, pp.pedido_id, pp.produto_id, pr.valor, pr.nome, pp.quantidade FROM pedido_produto pp INNER JOIN produtos pr ON pp.produto_id=pr.produto_id INNER JOIN pedidos p ON pp.pedido_id=p.pedido_id INNER JOIN mesas m ON pp.pedido_id=m.pedido_id WHERE m.mesa_id = %s", (id,))
        conn.commit()
        lists = cursor.fetchall()
        return lists 
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
    
def remove_food():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        pedido_id = int(input("Digite o id do pedido: "))
        lists = list_food(pedido_id)
        print(f"x------------PEDIDO ID: {pedido_id} ---------------x")
        total = 0
        for order in lists:
            print(f"P{order[3]} - R${order[4]} {order[5]} x {order[6]}")
            total = total + order[4] * order[6]
        print(f"Total: R${total:.2f}")
        print("x-----------------------------------------x")
        produto_id = int(input("Digite o id do produto que deseja excluir: "))
        cursor.execute("DELETE FROM pedido_produto WHERE pedido_id=%s AND produto_id=%s", (pedido_id, produto_id))
        conn.commit()
        print(f"Pedido: P{produto_id} removido!")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()

def update_food(waiter_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        print("Qual pedido/produto deseja alterar? ")
        cursor.execute("SELECT pp.pedido_id, pr.produto_id, pr.nome, pp.quantidade FROM  pedido_produto pp INNER JOIN produtos pr ON pp.produto_id=pr.produto_id INNER JOIN pedidos p ON pp.pedido_id=p.pedido_id ")
        conn.commit()
        orders = cursor.fetchall()
        print("PEDIDOS:")
        for order in orders:
            print(f"N°{order[0]}: ({order[1]}) - {order[2]} x {order[3]}")

        pedido_id = int(input("Digite o id do pedido que quer alterar: "))
        produto_id = int(input("Digite o id do produto: "))
        cursor.execute("SELECT valor FROM produtos")
        conn.commit()
        value = cursor.fetchall()
        print(f"1 - Pizza de frango R${value[0]}\n2 - Pizza de camarão R${value[1]}\n3 - Pizza de calabresa R${value[2]}\n4 - Coca-cola R${value[3]}\n5 - Água s/gás R${value[4]}")
        print("O que será alterado? ")
        new_produto_id = int(input("Digite qual será o novo produto: "))
        quantity = int(input("Digite quantos deseja: "))
        cursor.execute("UPDATE pedido_produto SET produto_id = %s, quantidade = %s WHERE pedido_id = %s AND produto_id = %s", (new_produto_id, quantity, pedido_id, produto_id))
        conn.commit()
        print("Alterado!")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
