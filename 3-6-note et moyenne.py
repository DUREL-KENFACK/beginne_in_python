moyenne=float(input("entrer votre note :"))
#verifie que la note est valid(s)
if moyenne<10:
    print("tu es recaler")
elif 10<=moyenne and moyenne<12:
    print("mention passable")
elif 12<=moyenne and moyenne<14:
    print("mention assez bien")
elif 14<=moyenne and moyenne<16:
    print("mantion bien")
elif 16<=moyenne:
    print("tres bien")