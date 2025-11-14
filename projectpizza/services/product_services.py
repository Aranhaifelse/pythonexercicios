from config.bd import create_connection
def ask_food(garcom_id):
    try:
    while True:    
        print("1 - Pizza de frango R$22.99\n2 - Pizza de camarão R$30.00\n3 - Pizza de calabresaR$20.00")
        pedido = int(input("Digite um número para escolher: "))
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedidos(garcom_id) VALUES (%s)", (garcom_id,))
        cursor.execute("INSERT INTO pedido_produto(pedido_id, produto_id) VALUES (%s, %s)", (garcom_id, pedido))
        conn.commit()
        resp = input("Deseja mais algo? (s/n)").lower()
        if resp == 's':
            continue
        elif resp == 'n':
            break