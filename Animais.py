def listarAnimais():
    if len(animais) == 0:
        print("Não tem animais cadastrados")
    for p in animais:
       print(f"{p['nome']} - {p['tipo']} | {p['raca']} | {p['idade']} anos")


def adicionarAnimais(animal):
    if not animal.get("nome"):
        return False
    if not animal.get("idade"):
        return False
    if not animal.get("raca"):
        return False
    if not animal.get("tipo"):
        return False
    animais.append(animal)
    return True


def buscarAnimais(animaisNome):
    for i, p in enumerate(animais):
        if p["nome"] == animaisNome:
            return i
    return None


def atualizarAnimais(indice, animais):
    animais[indice] = animais
    return True


def removerAnimais(indice):
    animais.pop(indice)


animais = []