def factoriel(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
nombre=int(input("Entre un nombre : "))
factoriel_nombr=factoriel(nombre)
print(f"le factoriel du nombre {nombre} est {factoriel_nombr}.")