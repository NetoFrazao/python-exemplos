alunos = ["Douglas"]
alunos.append("Rafael")
while True:
    nome = input("Digite o nome do aluno: ")
    alunos.append(alunos)
    resposta = input("Deseja adicionar mais um aluno? (S/N): ")
    if resposta.upper() == "N":
        break
print(f"Alunos cadastrados: {alunos}")
