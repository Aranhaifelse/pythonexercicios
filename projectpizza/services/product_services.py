from config.bd import create_connection
def ask_food(garcom_id):
        while True:    
            print("1 - Pizza de frango R$22.99\n2 - Pizza de camarão R$30.00\n3 - Pizza de calabresaR$20.00")
            produto_id = int(input("Digite um número para escolher: "))
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pedidos(garcom_id) VALUES (%s)", (garcom_id,))
            cursor.execute("SELECT * FROM pedidos WHERE garcom_id = %s", (garcom_id,))
            pedido_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO pedido_produto(pedido_id, produto_id) VALUES (%s, %s)", (pedido_id, produto_id))
            conn.commit()
            resp = input("Deseja mais algo? (s/n)").lower()
            if resp == 's':
                continue
            elif resp == 'n':
                break