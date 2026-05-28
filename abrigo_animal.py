from conexao import conectar
import os
import re
from datetime import datetime
 
 
def limpar_tela():
    os.system("cls")
 
 
def pausar():
    input("\nPressione ENTER para continuar...")
 
 
# ---------------- VALIDADORES ----------------
def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
 
    if len(cpf) != 11:
        return False
 
    if cpf == cpf[0] * 11:
        return False
 
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto
 
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto
 
    return cpf[-2:] == f"{digito1}{digito2}"
 
 
def validar_email(email: str) -> bool:
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))
 
 
def validar_data(data: str) -> bool:
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except:
        return False
 
 
def input_cpf(mensagem: str) -> str:
    while True:
        cpf = input(mensagem)
        if validar_cpf(cpf):
            return cpf
        print("CPF inválido! Tente novamente.")
 
 
def input_email(mensagem: str) -> str:
    while True:
        email = input(mensagem)
        if validar_email(email):
            return email
        print("Email inválido! Tente novamente.")
 
 
def input_data(mensagem: str) -> str:
    while True:
        data = input(mensagem)
        if validar_data(data):
            return data
        print("Data inválida! Use o formato ano-mes-dia (ex: 2020-05-25). Tente novamente.")
 
 
# ---------------- ANIMAIS ----------------
def cadastrar_animal(nome, raca, data_nascimento, especie, sexo, porte):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = """
    INSERT INTO tbl_animal
    (nome_animal, especie_animal, raca_animal, data_nascimento, sexo_animal, porte_animal, status_animal)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
 
    valores = (nome, especie, raca, data_nascimento, sexo, porte, 0)
 
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
 
    print("Animal cadastrado com sucesso!")
 
 
def buscar_animal(id_animal):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = "SELECT * FROM tbl_animal WHERE id_animal = %s"
    cursor.execute(sql, (id_animal,))
    animal = cursor.fetchone()
 
    cursor.close()
    conexao.close()
 
    return animal
 
 
def listar_animais():
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = "SELECT * FROM tbl_animal"
    cursor.execute(sql)
    dados = cursor.fetchall()
 
    if not dados:
        print("Nenhum animal cadastrado.")
 
    for animal in dados:
        data_nascimento = animal[4]
 
        if data_nascimento:
            hoje = datetime.now()
            idade = hoje.year - data_nascimento.year
            if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1
            info_idade = f"{data_nascimento.strftime('%d/%m/%Y')} ({idade} ano(s))"
        else:
            info_idade = "Não informada"
 
        print(f"""
    ID: {animal[0]}
    Nome: {animal[1]}
    Espécie: {animal[2]}
    Raça: {animal[3]}
    Data Nascimento / Idade: {info_idade}
    Sexo: {animal[5]}
    Porte: {animal[6]}
    Status: {"Adotado" if animal[7] == 1 else "Disponível"}
    =================================
    """)
 
 
# ---------------- ADOTANTE ----------------
def cadastrar_adotante(nome, cpf, telefone, email, cep, logradouro, complemento):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = """
    INSERT INTO tbl_adotante
    (nome_adotante, cpf_adotante, telefone_adotante, email_adotante,
    cep_adotante, logradouro_adotante, complemento_adotante)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
 
    valores = (nome, cpf, telefone, email, cep, logradouro, complemento)
 
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
 
    print("Adotante cadastrado com sucesso!")
 
 
def listar_adotantes():
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = "SELECT * FROM tbl_adotante"
    cursor.execute(sql)
    dados = cursor.fetchall()
 
    if not dados:
        print("Nenhum adotante cadastrado.")
 
    for adotante in dados:
        print(f"""
ID: {adotante[0]}
Nome: {adotante[1]}
Telefone: {adotante[2]}
CPF: {adotante[3]}
Email: {adotante[4]}
CEP: {adotante[5]}
Logradouro: {adotante[6]}
Complemento: {adotante[7]}
=================================
""")
 
    cursor.close()
    conexao.close()
 
 
# ---------------- ADOÇÃO ----------------
def solicitar_adocao(id_adotante, id_animal):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql_animal = "SELECT * FROM tbl_animal WHERE id_animal = %s"
    cursor.execute(sql_animal, (id_animal,))
    animal = cursor.fetchone()
 
    if not animal:
        print("Erro: Animal não existe.")
        cursor.close()
        conexao.close()
        return
 
    if animal[7] == 1:
        print("Erro: Este animal já foi adotado.")
        cursor.close()
        conexao.close()
        return
 
    sql_update = """
    UPDATE tbl_animal
    SET status_animal = 1,
        id_adotante = %s
    WHERE id_animal = %s
    """
 
    cursor.execute(sql_update, (id_adotante, id_animal))
    conexao.commit()
 
    print("Adoção solicitada com sucesso!")
 
    cursor.close()
    conexao.close()
 
 
def listar_adocoes():
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = """
    SELECT
        tbl_adotante.nome_adotante,
        tbl_animal.nome_animal
    FROM tbl_animal
    INNER JOIN tbl_adotante
    ON tbl_animal.id_adotante = tbl_adotante.id_adotante
    WHERE tbl_animal.status_animal = 1
    """
 
    cursor.execute(sql)
    dados = cursor.fetchall()
 
    if not dados:
        print("Nenhuma adoção registrada.")
 
    for adocao in dados:
        print(f"""
Adotante: {adocao[0]}
Animal: {adocao[1]}
=================================
""")
 
    cursor.close()
    conexao.close()
 
 
# ---------------- ATUALIZAR ANIMAL ----------------
def atualizar_animal(id_animal, nome, raca, data_nascimento, especie, sexo, porte):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = """
    UPDATE tbl_animal
    SET nome_animal = %s,
        especie_animal = %s,
        raca_animal = %s,
        data_nascimento = %s,
        sexo_animal = %s,
        porte_animal = %s
    WHERE id_animal = %s
    """
 
    valores = (nome, especie, raca, data_nascimento, sexo, porte, id_animal)
 
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
 
    print("Animal atualizado com sucesso!")
 
 
# ---------------- ATUALIZAR ADOTANTE ----------------
def atualizar_adotante(id_adotante, nome, cpf, telefone, email, cep, logradouro, complemento):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql = """
    UPDATE tbl_adotante
    SET nome_adotante = %s,
        cpf_adotante = %s,
        telefone_adotante = %s,
        email_adotante = %s,
        cep_adotante = %s,
        logradouro_adotante = %s,
        complemento_adotante = %s
    WHERE id_adotante = %s
    """
 
    valores = (nome, cpf, telefone, email, cep, logradouro, complemento, id_adotante)
 
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
 
    print("Adotante atualizado com sucesso!")
 
 
def excluir_animal(id_animal):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql_atendimento = "DELETE FROM tbl_atendimento WHERE id_animal = %s"
    cursor.execute(sql_atendimento, (id_animal,))
 
    sql_vacina = "DELETE FROM tbl_vacina WHERE id_animal = %s"
    cursor.execute(sql_vacina, (id_animal,))
 
    sql_animal = "DELETE FROM tbl_animal WHERE id_animal = %s"
    cursor.execute(sql_animal, (id_animal,))
 
    conexao.commit()
    cursor.close()
    conexao.close()
 
    print("Animal excluído com sucesso!")
 
 
# ---------------- EXCLUIR ADOTANTE ----------------
def excluir_adotante(id_adotante):
    conexao = conectar()
    cursor = conexao.cursor()
 
    sql_update = """
    UPDATE tbl_animal
    SET id_adotante = NULL
    WHERE id_adotante = %s
    """
    cursor.execute(sql_update, (id_adotante,))
 
    sql_delete = "DELETE FROM tbl_adotante WHERE id_adotante = %s"
    cursor.execute(sql_delete, (id_adotante,))
 
    conexao.commit()
    cursor.close()
    conexao.close()
 
    print("Adotante excluído com sucesso!")
 
 
# ---------------- ATUALIZAR ADOÇÃO ----------------
def atualizar_adocao(id_animal, novo_id_adotante):
    conexao = conectar()
    cursor = conexao.cursor()
 
    cursor.execute("SELECT * FROM tbl_animal WHERE id_animal = %s", (id_animal,))
    animal = cursor.fetchone()
 
    if not animal:
        print("Animal não encontrado.")
        cursor.close()
        conexao.close()
        return
 
    cursor.execute("SELECT * FROM tbl_adotante WHERE id_adotante = %s", (novo_id_adotante,))
    adotante = cursor.fetchone()
 
    if not adotante:
        print("Adotante não encontrado.")
        cursor.close()
        conexao.close()
        return
 
    cursor.execute("UPDATE tbl_animal SET id_adotante = %s WHERE id_animal = %s", (novo_id_adotante, id_animal))
 
    conexao.commit()
    cursor.close()
    conexao.close()
 
    print("Adoção atualizada com sucesso!")
 
 
# ---------------- MENU PRINCIPAL ----------------
opcao = None
 
while opcao != "0":
    limpar_tela()
 
    print("========================================")
    print("        SISTEMA DE ADOÇÃO DE ANIMAIS")
    print("========================================")
    print("1 - Listar Animais")
    print("2 - Cadastrar Animal")
    print("3 - Cadastrar Adotante")
    print("4 - Solicitar Adoção")
    print("5 - Listar Adoções")
    print("6 - Listar Adotantes")
    print("7 - Atualizar Animal")
    print("8 - Atualizar Adotante")
    print("9 - Excluir Animal")
    print("10 - Excluir Adotante")
    print("11 - Atualizar Adoção")
    print("0 - Sair")
    print("========================================")
 
    opcao = input("Opção desejada: ")
 
    limpar_tela()
 
    if opcao == "1":
        print("LISTA DE ANIMAIS =======================\n")
        listar_animais()
        pausar()
 
    elif opcao == "2":
        print("CADASTRAR ANIMAL =======================\n")
 
        nome = input("Nome: ")
        raca = input("Raça: ")
        data_nascimento = input_data("Data de Nascimento (ano-mes-dia): ")
 
        print("\nEspécie:")
        print("1 - Cachorro")
        print("2 - Gato")
 
        opcao_especie = input("Escolha: ")
 
        if opcao_especie == "1":
            especie = "Cachorro"
        elif opcao_especie == "2":
            especie = "Gato"
        else:
            print("Opção inválida.")
            pausar()
            continue
 
        print("\nSexo:")
        print("1 - Macho")
        print("2 - Fêmea")
 
        opcao_sexo = input("Escolha: ")
 
        if opcao_sexo == "1":
            sexo = "Macho"
        elif opcao_sexo == "2":
            sexo = "Fêmea"
        else:
            print("Opção inválida.")
            pausar()
            continue
 
        print("\nPorte:")
        print("1 - Pequeno")
        print("2 - Médio")
        print("3 - Grande")
 
        opcao_porte = input("Escolha: ")
 
        if opcao_porte == "1":
            porte = "Pequeno"
        elif opcao_porte == "2":
            porte = "Médio"
        elif opcao_porte == "3":
            porte = "Grande"
        else:
            print("Opção inválida.")
            pausar()
            continue
 
        cadastrar_animal(nome, raca, data_nascimento, especie, sexo, porte)
        pausar()
 
    elif opcao == "3":
        print("CADASTRAR ADOTANTE =====================\n")
 
        nome = input("Nome: ")
        cpf = input_cpf("CPF: ")
        telefone = input("Telefone: ")
        email = input_email("Email: ")
        cep = input("CEP: ")
        logradouro = input("Logradouro: ")
        complemento = input("Complemento: ")
 
        cadastrar_adotante(nome, cpf, telefone, email, cep, logradouro, complemento)
        pausar()
 
    elif opcao == "4":
        print("SOLICITAR ADOÇÃO =======================\n")
 
        try:
            id_adotante = int(input("ID do adotante: "))
            id_animal = int(input("ID do animal: "))
            print()
            solicitar_adocao(id_adotante, id_animal)
        except ValueError:
            print("\nErro: Os IDs devem ser números inteiros.")
 
        pausar()
 
    elif opcao == "5":
        print("LISTA DE ADOÇÕES =======================\n")
        listar_adocoes()
        pausar()
 
    elif opcao == "6":
        print("LISTA DE ADOTANTES =====================\n")
        listar_adotantes()
        pausar()
 
    elif opcao == "7":
        print("ATUALIZAR ANIMAL ======================\n")
 
        try:
            id_animal = int(input("ID do animal: "))
 
            nome = input("Novo nome: ")
            raca = input("Nova raça: ")
            data_nascimento = input_data("Nova data de nascimento (ano-mes-dia): ")
 
            print("\nEspécie:")
            print("1 - Cachorro")
            print("2 - Gato")
 
            opcao_especie = input("Escolha: ")
 
            if opcao_especie == "1":
                especie = "Cachorro"
            elif opcao_especie == "2":
                especie = "Gato"
            else:
                print("Opção inválida.")
                pausar()
                continue
 
            print("\nSexo:")
            print("1 - Macho")
            print("2 - Fêmea")
 
            opcao_sexo = input("Escolha: ")
 
            if opcao_sexo == "1":
                sexo = "Macho"
            elif opcao_sexo == "2":
                sexo = "Fêmea"
            else:
                print("Opção inválida.")
                pausar()
                continue
 
            print("\nPorte:")
            print("1 - Pequeno")
            print("2 - Médio")
            print("3 - Grande")
 
            opcao_porte = input("Escolha: ")
 
            if opcao_porte == "1":
                porte = "Pequeno"
            elif opcao_porte == "2":
                porte = "Médio"
            elif opcao_porte == "3":
                porte = "Grande"
            else:
                print("Opção inválida.")
                pausar()
                continue
 
            atualizar_animal(id_animal, nome, raca, data_nascimento, especie, sexo, porte)
 
        except ValueError:
            print("Erro: ID inválido.")
 
        pausar()
 
    elif opcao == "8":
        print("ATUALIZAR ADOTANTE ====================\n")
 
        try:
            id_adotante = int(input("ID do adotante: "))
 
            nome = input("Novo nome: ")
            cpf = input_cpf("Novo CPF: ")
            telefone = input("Novo telefone: ")
            email = input_email("Novo email: ")
            cep = input("Novo CEP: ")
            logradouro = input("Novo logradouro: ")
            complemento = input("Novo complemento: ")
 
            atualizar_adotante(id_adotante, nome, cpf, telefone, email, cep, logradouro, complemento)
 
        except ValueError:
            print("Erro: ID inválido.")
 
        pausar()
 
    elif opcao == "9":
        print("EXCLUIR ANIMAL ========================\n")
 
        try:
            id_animal = int(input("ID do animal: "))
            confirmar = input("Tem certeza que deseja excluir este animal? (s/n): ").lower()
 
            if confirmar == "s":
                excluir_animal(id_animal)
            else:
                print("Exclusão cancelada.")
 
        except ValueError:
            print("Erro: ID inválido.")
 
        pausar()
 
    elif opcao == "10":
        print("EXCLUIR ADOTANTE ======================\n")
 
        try:
            id_adotante = int(input("ID do adotante: "))
            confirmar = input("Tem certeza que deseja excluir este adotante? (s/n): ").lower()
 
            if confirmar == "s":
                excluir_adotante(id_adotante)
            else:
                print("Exclusão cancelada.")
 
        except ValueError:
            print("Erro: ID inválido.")
 
        pausar()
 
    elif opcao == "11":
        print("ATUALIZAR ADOÇÃO ======================\n")
 
        try:
            id_animal = int(input("ID do animal: "))
            novo_id_adotante = int(input("Novo ID do adotante: "))
            atualizar_adocao(id_animal, novo_id_adotante)
 
        except ValueError:
            print("Erro: IDs inválidos.")
 
        pausar()
 
    elif opcao == "0":
        print("Saindo do sistema...")
 
    else:
        print("Opção inválida!")
        pausar()