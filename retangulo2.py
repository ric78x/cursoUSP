
l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

largura = 0
altura = 0

while altura < a:
    while largura < l:
        print("#", end = "")
        largura = largura + 1
    altura = altura + 1
    print ()
    largura = 0