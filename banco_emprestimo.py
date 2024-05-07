print(f"Programa de emprestimo\n"
      f"Responda:  (0-Nao ou 1-Sim)")
nome_negativado=int(input("Possui nome negativado?: "))
if nome_negativado == 1:
    print("Nao pode realizar emprestimo")
else:
    carteira_assinada=int(input("Possui carteira assinada?: "))
    if carteira_assinada == 0:
        print("Nao pode realizar emprestimo")
    else:
        casa_propria=int(input("Possui casa propria?: "))
        if casa_propria == 0:
            print("Nao pode realizar emprestimo")
        else:
            print("Conceder emprestimo")