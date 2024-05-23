import random
alunos=["Joao", "Maria", "Felipe", "Ana", "Lucas", "Mariana"]
print(f"Lista: {alunos}")
# Embaralhar a Lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Ordena a Lista Crescente
alunos.sort()
print(f"Lista crescente: {alunos}")
# Ordena a Lista Decrescente 
alunos.sort(reverse=True)
print(f"Lista decrescente: {alunos}")