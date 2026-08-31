from database import conectar


def criar_usuario():
    print("\n===================================")
    print("       CRIAR PERFIL")
    print("===================================\n")

    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    profissao = input("Profissão: ")
    curso = input("Curso/Área de estudo: ")

    personalidade = input(
        "Como você descreve sua personalidade? "
    )

    emocao = input(
        "Quais emoções você sente com mais frequência? "
    )

    atividade_humor = input(
        "O que normalmente melhora seu humor? "
    )

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios
        (
            nome,
            idade,
            cidade,
            profissao,
            curso,
            personalidade,
            emocao_frequente,
            atividade_humor
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        nome,
        idade,
        cidade,
        profissao,
        curso,
        personalidade,
        emocao,
        atividade_humor
    ))

    usuario_id = cursor.lastrowid

    conexao.commit()
    conexao.close()

    print("\nPerfil criado com sucesso!")
    print(f"ID do usuário: {usuario_id}")

    return usuario_id


def buscar_usuario(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM usuarios
        WHERE id = ?
    """, (usuario_id,))

    usuario = cursor.fetchone()

    conexao.close()

    return usuario
