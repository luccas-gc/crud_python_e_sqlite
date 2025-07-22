import crud
import verificadores

def verify_option(option):
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()

def option1():
    username = input("Nome do usuário: ")
    profession = input("Profissão: ")

    check_inputs = verificadores.check_input(username, profession)

    if check_inputs == True:
        new_user = crud.User(username, profession)
        try:
            crud.table.add_user(new_user)
        except crud.ErrorDB as e:
            print(e)
    else:
        print("\nErro: Entrada inválida.")

def option2():
    try:
        registers = crud.table.read_user()
        if registers:
            for id, nome, profession in registers:
                print(f"ID: {id} | Nome: {nome} | Profissão: {profession}")
        else:
            print("Nenhum usuário cadastrado.")
    except crud.ErrorDB as e:
            print(e)

def option3():
    update_option = str(input("\nN - Atualizar Nome\nP - Atualizar Profisão\nA - Atualizar todos os dados\n\nSelecione uma Opcao: ")).lower()
    
    check_update_option = verificadores.check_sub_option(update_option)
    
    if check_update_option == True:
        if update_option == "n":
            update_id = int(input("ID do Usuário: "))
            update_nome = str(input("Novo Nome: "))

            verify_input = verificadores.check_input(update_nome, None)

            if verify_input == True:
                verify_user = verificadores.check_user_exists(update_id)

                if verify_user == True:
                    try:
                        crud.table.update_user(update_id, update_nome)
                    except crud.ErrorDB as e:
                        print(e)
                else:
                    print("ID de Usuário inexistente.")
            else: 
                print("Erro: Entrada Inválida.")

        elif update_option == "p":
            update_id = int(input("ID do Usuário: "))
            update_profession = str(input("Nova Profissão: "))

            verify_input = verificadores.check_input(None, update_profession)

            if verify_input == True:
                verify_user = verificadores.check_user_exists(update_id)

                if verify_user == True:
                    try:
                        crud.table.update_user(update_id, update_profession)
                    except crud.ErrorDB as e:
                        print(e)
                else:
                    print("ID de Usuário inexistente.")
            else: 
                print("Erro: Entrada Inválida.")

        elif update_option == "a":
            update_id = int(input("ID do Usuário: "))
            update_nome = str(input("Novo Nome: "))
            update_profession = str(input("Nova Profissão: "))

            verify_input = verificadores.check_input(update_nome, update_profession)

            if verify_input == True:
                verify_user = verificadores.check_user_exists(update_id)

                if verify_user == True:
                    try:
                        crud.table.update_user(update_id, update_nome, update_profession)
                    except crud.ErrorDB as e:
                        print(e)
                else:
                    print("ID de Usuário inexistente.")
            else:
                print("Erro: Entrada Inválida.")

def option4():
    delete_id = int(input("ID do Usuário: "))
    try:
        crud.table.delete_user(delete_id)
    except crud.ErrorDB as e:
        print(e)

def option5():
    print("Encerrando...")
    exit()
