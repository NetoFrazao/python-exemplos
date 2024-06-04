def exibirMensagem(nome):
    print(f"Seja bem vindo {nome}")
    return f"Usuario logado: {nome}"

usuario = exibirMensagem("Joao")
print(usuario)