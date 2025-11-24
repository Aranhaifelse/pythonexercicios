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
              id_mesa = int(input("Digite o id da mesa: "))
              lists = list_food(id_mesa)
              print(f"x------------MESA N°: {id_mesa} ---------------x")
              total = 0
              for order in lists:
                print(f"R${order[4]} {order[5]} x {order[6]}")
                total = total + order[4] * order[6]
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
                update_value()
        elif opcao == 3:
                break
              

