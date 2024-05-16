print("Operação de Divisao")
while True:
    n1=int(input("Informe o primeiro numero: "))
    n2=int(input("Informe o segundo numero: "))
    if n2 == 0:
        print("Divisor nao pode ser 0")
        break
    print(f"{n1} / {n2} = {n1/n2}")
    print(f"{20 * "-"}")
print("Fim do programa")