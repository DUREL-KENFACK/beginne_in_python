a=int(input("entrer a :"))
b=int(input("entrer b :"))
if a==0 or b==0:
    print(f"le produit de {a} et {b} est nul")
elif (a<0 and b>0) or (a > 0 and b<0):
    print(f"le produit de {a} et {b} est negatif")
elif a<0 and b<0:
    print(f"le produit de {a} et {b} est positif")
else:
    print(f"le produit de {a} et {b} est positif")