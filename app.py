from database import criar_banco

from modules.usuarios import (
    criar_usuario,
    buscar_usuario
)

from modules.objetivos import (
    adicionar_objetivo,
    listar_objetivos
)

from modules.checkins import (
    realizar_checkin
)

from modules.espelho import (
    analisar_situacao
)


def menu_principal(usuario_id):

    while True:

        usuario = buscar_usuario(usuario_id)

        print("\n")
        print("======================================")
        print("          KARMA ESPELHO")
        print("======================================")

        print(f"Olá, {usuario[1]}!")

        print("\n1 - Check-in emocional")
        print("2 - Meus objetivos")
        print("3 - Adicionar objetivo")
        print("4 - Espelho de consequências")
        print("5 - Meu perfil")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            realizar_checkin(usuario_id)

        elif opcao == "2":
            listar_objetivos(usuario_id)

        elif opcao == "3":
            adicionar_objetivo(usuario_id)

        elif opcao == "4":
            analisar_situacao()

        elif opcao == "5":
            mostrar_perfil(usuario)

        elif opcao == "0":
            print("\nAté logo.")
            break

        else:
            print("\nOpção inválida.")


def mostrar_perfil(usuario):

    print("\n===================================")
    print("            MEU PERFIL")
    print("===================================\n")

    print(f"Nome: {usuario[1]}")
    print(f"Idade: {usuario[2]}")
    print(f"Cidade: {usuario[3]}")
    print(f"Profissão: {usuario[4]}")
    print(f"Curso: {usuario[5]}")
    print(f"Personalidade: {usuario[6]}")
    print(f"Emoções frequentes: {usuario[7]}")
    print(f"O que melhora o humor: {usuario[8]}")


def iniciar():

    criar_banco()

    print("======================================")
    print("          KARMA ESPELHO")
    print("======================================")

    print("\n1 - Criar novo perfil")
    print("2 - Entrar")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        usuario_id = criar_usuario()

        menu_principal(usuario_id)

    elif opcao == "2":

        try:
            usuario_id = int(
                input("Digite seu ID de usuário: ")
            )

            usuario = buscar_usuario(usuario_id)

            if usuario:
                menu_principal(usuario_id)
            else:
                print("\nUsuário não encontrado.")

        except ValueError:
            print("\nID inválido.")

    else:
        print("\nOpção inválida.")


if __name__ == "__main__":
    iniciar()
