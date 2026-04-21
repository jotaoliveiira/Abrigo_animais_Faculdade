def listarAnimais():
    if len(animais) == 0:
        print("Não tem produtos cadastrados")
    for p in animais:
        print(f"{p['nome']}")


def adicionarAnimais(animais):
    if not animais["nome"]:
        return False
    animais.append(animais)
    return True


def buscarAnimais(animaisNome):
    for i, p in enumerate(animais):
        if p["nome"] == animaisNome:
            return i
    return None


def atualizarAnimais(indice, produto):
    animais[indice] = animais
    return True


def removerAnimais(indice):
    animais.pop(indice)


animais = []