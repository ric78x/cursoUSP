
l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

largura = 0
altura = 0

while altura < a:
    while largura < l:
        while largura > 0 and largura < l-1 and altura > 0 and altura < a-1:
            print(" ", end = "")
            largura = largura + 1
        print("#", end = "")
        largura = largura + 1
    altura = altura + 1
    print ()
    largura = 0