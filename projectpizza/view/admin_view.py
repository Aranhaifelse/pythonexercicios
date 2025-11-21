from config.bd import create_connection
from services.admin_services import insert_product, update_value
from services.product_services import ask_food, list_food, remove_food, update_food
def panel(waiter_auth):
    while True:
        print("X---------------PAINEL DE PEDIDOS--------------X")
        print("1 - Inserir pedidos\n2 - Listar pedidos\n3 - Remover pedido\n4 - Atualizar pedido\n5 - Sair do sistema")
        opcao = int(input("Selecione um número: "))
        if opcao == 1:
                ask_food(waiter_auth[0])  
        elif opcao == 2:
              id_pedido = int(input("Digite o id do pedido: "))
              lists = list_food(id_pedido)
              print(f"x------------PEDIDO ID: {id_pedido} ---------------x")
              total = 0
              for order in lists:
                print(f"R${order[2]} {order[3]} x {order[4]}")
                total = total + order[2] * order[4]
              print(f"Total: R${total:.2f}")
              print("x-----------------------------------------x")  
        elif opcao == 3:
                remove_food()
        elif opcao == 4:
                update_food(waiter_auth[0])
        elif opcao == 5:
                break

def panel_admin():
    while True:
        print("1 - Inserir produtos\n 2 - Atualizar preço \n 3 - Sair do sistema")
        opcao = int(input("Escolha:"))
        if opcao == 1:
                valor = float(input("Digite o valor da comida: "))
                nome = input("Digite o nome da comida: ")
                insert_product(valor, nome)
        elif opcao == 2:
                id_product = int(input("Digite o id do produto: "))
                new_value = float(input("Digite o novo valor: "))
                update_value(id_product, new_value)
        elif opcao == 3:
                break
              

