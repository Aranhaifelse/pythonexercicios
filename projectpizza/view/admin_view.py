from config.bd import create_connection
from services.admin_services import insert_product
from services.product_services import ask_food
def panel(user_auth):
    while True:
        print("1 - Relacionar mesa/Inserir pedidos \n 3 - Listar pedidos \n 3 - Remover/Atualizar pedido\n 4 - Sair do sistema")
        opcao = int(input("Selecione um número: "))
        if opcao == 1:
                ask_food(user_auth[0])  
        elif opcao == 5:
                break




# def panel_admin():
#     print("1 - Inserir produtos\n 2 - Atualizar preço \n 4 - Sair do sistema")
#     opcao = input("Escolha:")
#     if opcao == 1:
#         valor = float(input("Digite o valor da comida: "))
#         nome = input("Digite o nome da comida: ")
#         insert_product(valor, nome)
#     elif opcao == 2:
#         id_product = int(input("Digite o id do produto: "))
#         new_value = float(input("Digite o novo valor: "))

