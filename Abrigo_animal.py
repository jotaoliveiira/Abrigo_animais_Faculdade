animais = []
adotantes = []
adocoes = []

# ---------------- ANIMAIS ----------------
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


def buscar_animal(id):
    for animal in animais:
        if animal["id"] == id:
            return animal
    return None


# ---------------- ADOTANTE ----------------
def cadastrar_adotante(id, nome, cpf, telefone):
    adotante = {
        "id": id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone
    }
    adotantes.append(adotante)
    print("Adotante cadastrado!")


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










   