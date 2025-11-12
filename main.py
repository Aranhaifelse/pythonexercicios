from services.user_services import login_user
while True: 
    print("1 - Cadastrar funcionário \n 2 - Cadastrar administrador \n 3 - Entrar \n 4 - Sair")
    opcao = int(input("Selecione um número: "))
    
    if opcao == 1: 
        email = input("Digite um email: ")
        password = input("Digite uma senha: ")
        login_user(email, password)
    elif opcao == 2:
        email = input("Digite um email: ")
        password = input("Digite uma senha: ")
        login_admin(email, password)