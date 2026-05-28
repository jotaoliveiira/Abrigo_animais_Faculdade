

# ---------------- ANIMAIS ----------------
def cadastrar_animal(id, nome, especie, raca, idade):
    animal = {
        "id": id,
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "status": "disponivel"
    }
    animais.append(animal)
    print("Animal cadastrado!")


def buscar_animal(id):
    for animal in animais:
        if animal["id"] == id:
            return animal
    return None


def listar_animais():
    if not animais:
        print("Nenhum animal cadastrado.")
    for animal in animais:
        print(animal)


# ---------------- ADOTANTE ----------------
def cadastrar_adotante(id, nome, cpf, telefone, email, senha):
    adotante = {
        "id": id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone
        

    }
    adotantes.append(adotante)
    print("Adotante cadastrado!")



def listar_adotantes():
    if not adotantes:
        print("Nenhum adotante cadastrado.")
    for a in adotantes:
        print(a)

# ---------------- ADOÇÃO ----------------
def solicitar_adocao(id_adotante, id_animal):
    animal = buscar_animal(id_animal)

    if not animal:
        print("Animal não existe")
        return

    if animal["status"] == "adotado":
        print("Animal já foi adotado")
        return

    adocao = {
        "adotante_id": id_adotante,
        "animal_id": id_animal,
        "status": "pendente"
    }

    adocoes.append(adocao)
    print("Adoção solicitada!")




def listar_adocoes():
    if not adocoes:
        print("Nenhuma adoção registrada.")
    for a in adocoes:
        print(a)



animais = []
adotantes = []
adocoes = []

opcao = None

while opcao != "0":
    print()
    print("========================================")
    print("        SISTEMA DE ADOÇÃO")
    print("========================================")
    print("1 - Listar Animais")
    print("2 - Cadastrar Animal")
    print("3 - Cadastrar Adotante")
    print("4 - Solicitar Adoção")
    print("5 - Listar Adoções")
    print("6 - Listar Adotantes")
    print("0 - Sair")
    print("========================================")

    opcao = input("Opção desejada: ")

    if opcao == "1":
        print()
        print("LISTA DE ANIMAIS =======================")
        listar_animais()

    elif opcao == "2":
        print()
        print("CADASTRAR ANIMAL =======================")
        id = int(input("ID: "))
        nome = input("Nome: ")
        especie = input("Espécie: ")
        raca = input("Raça: ")
        idade = int(input("Idade: "))
        cadastrar_animal(id, nome, especie, raca, idade)

    elif opcao == "3":
        print()
        print("CADASTRAR ADOTANTE =====================")
        id = int(input("ID: "))
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cadastrar_adotante(id, nome, cpf, telefone, email, senha)

    elif opcao == "4":
        print()
        print("SOLICITAR ADOÇÃO =======================")
        id_adotante = int(input("ID do adotante: "))
        id_animal = int(input("ID do animal: "))
        solicitar_adocao(id_adotante, id_animal)

    elif opcao == "5":
        print()
        print("LISTA DE ADOÇÕES =======================")
        listar_adocoes()

    elif opcao == "6":
        print()
        print("LISTA DE ADOTANTES =====================")
        listar_adotantes()

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opção não existe")
