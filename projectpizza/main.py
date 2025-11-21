from services.user_services import insert_user,login
from view.admin_view import panel, panel_admin
while True: 
    print("X---------------PROJECT PIZZA--------------X")
    print("1 - Cadastrar\n2 - Entrar\n3 - Administrar produtos\n4 - Sair")
    opcao = int(input("Selecione um número: "))
    if opcao == 1: 
        email = input("Digite um email: ")
        password = input("Digite uma senha: ")
        name = input("Digite o nome completo: ")
        fone = input("Digite seu telefone: ")
        insert_user(email, password, name, fone)

    elif opcao == 2:
        email = input("Digite o email: ")
        password = input("Digite a senha: ")
        waiter_auth = login(email, password)
        if waiter_auth:
            panel(waiter_auth)
        else:
            print("Usuario ou senha inválidos")
    elif opcao == 3:
        email = input("Digite um email: ")
        password = input("Digite uma senha: ")
        waiter_auth = login(email, password)
        if waiter_auth: 
            panel_admin()
        else:
            print("Usuario ou senha inválidos")
    elif opcao == 4:
        break
