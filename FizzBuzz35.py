from math import sqrt

xA = float(input('Digite a abscissa do ponto A:'))
xB = float(input('Digite a abscissa do ponto B:'))

yA = float(input('Digite a ordenada do ponto A:'))
yB = float(input('Digite a abscissa do ponto B:'))

distAB = sqrt(((xA-xB)**2) + ((yA-yB)**2))


if distAB >= 10:
    print("longe")
else:
    print("perto")

