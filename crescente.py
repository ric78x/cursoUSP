numero = input("Digite um número inteiro: ")
numero2 = input("Digite um segundo número inteiro: ")
numero3 = input("Digite um terceiro número inteiro: ")
if int(numero) < int(numero2) and int(numero2) < int(numero3):
    print("crescente")
else:
    print("não está em ordem crescente")