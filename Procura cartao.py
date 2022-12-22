meucartao = int(input("Digite o numero do seu cartao de credito: "))

cartaolido = 1
encontreimeucartaonalista = False

while cartaolido != 0 and not encontreimeucartaonalista:
     cartaolido = int(input("Digite o numero do proximo cartao de credito: "))
     if cartaolido == meucartao:
          encontreimeucartaonalista = Tru

if encontreimeucartaonalista:
     print("SHOW!! Meu cartao esta la")
else:
     print("Ixi, Meu cartaao nao esta la")