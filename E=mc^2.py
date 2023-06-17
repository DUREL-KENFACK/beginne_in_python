#fonction pour resoudre l'equation E=mc^2
def equation():
    acceleration=float(input("entrer l'acceleration:"))
    masse=float(input("entrer la masse:"))
    energy=masse*square(acceleration)
    print(f"la solution de l'equation est:{energy}")


def square(n):
    return n*n


equation()
