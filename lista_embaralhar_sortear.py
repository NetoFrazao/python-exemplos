import random
alunos=["Joao", "Maria", "Felipe", "Ana", "Lucas", "Mariana"]
print(f"Lista: {alunos}")
# Embaralhar a Lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Escolhe um aluno aleatoriamente 
aluno_sorteado = random.choice(alunos)
print(f"Alunos sorteado: {aluno_sorteado}")