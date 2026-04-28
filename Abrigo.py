animais = []
adotante = []
adocoes = []


#ANIMAIS
def cadastrar_animal(id, nome, especie, idade):
    animal = {
        "id": id,
        "nome": nome,
        "especie": especie,
        "idade": idade,
        "status": "disponivel"
    }
    animais.append(animal)
    print("Animal cadastrado!")


def listar_animais():
    for animal in animais:
        print(animal)


def buscar_animal(id):
    for animal in animais:
        if animal["id"] == id:
            return animal
    return None


def atualizar_animal(id, nome):
    animal = buscar_animal(id)
    if animal:
        animal["nome"] = nome
        print("Atualizado!")
    else:
        print("Animal não encontrado")


def deletar_animal(id):
    for animal in animais:
        if animal["id"] == id:
            animais.remove(animal)
            print("Removido!")
            return
    print("Animal não encontrado")

    #ADOTANTE

    def cadastrar_adotante(id, nome, cpf, telefone):
        adotante = {
        "id": id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone
    }
    adotante.append(adotante)
    print("Adotante cadastrado!")


    def solicitar_adocao(nome_adotante, nome_animal):
        animal = buscar_animal(nome_animal)

    if not animal:
        print("Animal não existe")
        return

    if animal["status"] == "adotado":
        print("Animal já foi adotado")
        return

    adocao = {
        "adotante": nome_adotante,
        "animal": nome_animal,
        "status": "pendente"
    }

    adocoes.append(adocao)
    print("Adoção solicitada!")