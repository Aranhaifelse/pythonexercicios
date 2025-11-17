from services.user_services import insert_user,login
from view.admin_view import panel, panel_admin
while True: 
    print("1 - Cadastrar\n 2 - Entrar\n 3 - Administrar produtos\n  4 - Sair")
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
        user_auth = login(email, password)
        if user_auth:
            panel(user_auth)
        else:
            print("Usuario ou senha inválidos")
    elif opcao == 3:
        email = input("Digite um email: ")
        password = input("Digite uma senha: ")
        user_auth = login(email, password)
        if user_auth: 
            panel_admin()
        else:
            print("Usuario ou senha inválidos")
    elif opcao == 4:
        break
