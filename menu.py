import crud
import options

class OptionError(Exception): pass

crud.table.create_table()

def menu():
    while True:
        print("\n1. Adicionar Usuário\n2. Ver Registros\n3. Atualizar Usuário\n4. Deletar um usuário\n5. Sair")
        try:
            opcao = int(input("\nSelecione uma opção: "))
            if 1 <= opcao <= 5:
                options.verify_option(opcao)
            else:
                raise OptionError
            
        except ValueError:
            print("\nDigite um número.")
        except OptionError:
            print("\nDigite números entre 1 e 5.")

menu()