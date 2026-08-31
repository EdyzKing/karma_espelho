from database import conectar


def adicionar_objetivo(usuario_id):
    print("\n===================================")
    print("        NOVO OBJETIVO")
    print("===================================\n")

    objetivo = input("Digite seu objetivo: ")

    if not objetivo.strip():
        print("O objetivo não pode ficar vazio.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO objetivos (usuario_id, objetivo)
        VALUES (?, ?)
    """, (usuario_id, objetivo))

    conexao.commit()
    conexao.close()

    print("\nObjetivo registrado com sucesso!")


def listar_objetivos(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, objetivo, criado_em
        FROM objetivos
        WHERE usuario_id = ?
        ORDER BY id DESC
    """, (usuario_id,))

    objetivos = cursor.fetchall()

    conexao.close()

    print("\n===================================")
    print("          SEUS OBJETIVOS")
    print("===================================\n")

    if not objetivos:
        print("Nenhum objetivo cadastrado.")
        return

    for objetivo in objetivos:
        print(f"[{objetivo[0]}] {objetivo[1]}")
