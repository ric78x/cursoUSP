print("\n","Digite uma suencia de valores terminada por zero. ", "\n")

tamanho = int(input("Digite o tamanho da sequencia: "))

produto = 1

i = 0

while i < tamanho:
    valor = int(input(" Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("A Soma é : ", produto)