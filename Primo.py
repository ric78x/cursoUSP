def maior_primo(n):
    div=1
    val=True
    cont=0
    while div <=n and val:
        if n%div== 0:
            cont=cont+1
        if cont>=3:
            cont=1
            n=n-1
            div=1
        if cont==2 and n==div:
             val=False
        div=div+1
    return n