def rectangle():
    longuer=float(input("quel est la longuer du rectangle:"))
    largeur=float(input("quel est la largeur du recrangle:"))
    perimetre=somme(longuer,largeur)*2
    surface=produit(longuer,largeur)
    print(f"le perimetre du rectangle est de {perimetre}m et sa surface est  {surface}m^2 ")



def somme(x,n):
    return x+n
     
def produit(x,n):
    return x*n

rectangle()

