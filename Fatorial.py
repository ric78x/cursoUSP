n = int(input("Digite um número natural: "))

resultado=1
count=1

while count <= n:
    resultado *= count
    count += 1

print(resultado)