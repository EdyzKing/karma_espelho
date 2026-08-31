from database import conectar


def realizar_checkin(usuario_id):
    print("\n===================================")
    print("         CHECK-IN EMOCIONAL")
    print("===================================\n")

    print("De 1 a 10, como você está se sentindo agora?")
    
    while True:
        try:
            humor = int(input("Digite uma nota de 1 a 10: "))

            if 1 <= humor <= 10:
                break

            print("Digite um número entre 1 e 10.")

        except ValueError:
            print("Digite apenas números.")

    emocao = input("Qual emoção está mais presente agora? ")
    observacao = input("Quer contar o que está acontecendo? ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO checkins
        (
            usuario_id,
            humor,
            emocao,
            observacao
        )
        VALUES (?, ?, ?, ?)
    """, (
        usuario_id,
        humor,
        emocao,
        observacao
    ))

    conexao.commit()
    conexao.close()

    print("\nCheck-in registrado.")

    gerar_resposta(humor)


def gerar_resposta(humor):

    if humor <= 3:
        print("\nO Karma Espelho percebe que seu estado emocional")
        print("está abaixo do habitual.")
        print("Talvez seja um bom momento para fazer uma pausa")
        print("e cuidar um pouco de você.")

    elif humor <= 6:
        print("\nParece que você está em um estado emocional intermediário.")
        print("Observe o que está influenciando seu momento.")

    else:
        print("\nQue bom! Parece que você está tendo um")
        print("momento emocionalmente positivo.")
