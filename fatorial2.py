def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

print (fatorial(5))

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")

    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")

    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

print (testa_fatorial())