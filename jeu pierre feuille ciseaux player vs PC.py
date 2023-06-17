from random import randint
print("jeu de pierre,feuilleou ciseaux.")
tool=["pierre","feuille","ciseaux"]
pointsplayer=0
pointspc=0
pc=tool[randint(0,2)]
continuer=True
player=input("A vous de jouer : ")
while(continuer):
     if (player=="fin"):
        break
     elif (player== pc):
         print("match nul")
     elif(player==tool[0] and pc==tool[1]):
         print(f"vous avez perdu la" ,pc ,"emballe la",player)
         pointspc=pointspc+1
     elif(player==tool[1] and pc==tool[0]):
         print("vous avez gagne la",player ,"emballe la",pc)
         pointsplayer=pointsplayer+1
     elif(player==tool[2] and pc==tool[0]):
          print("vous avez perdu la",pc ,"ecrase le",player)
          pointspc=pointspc+1
     elif(player==tool[2] and pc==tool[1]):
          print("vous avez gagne le",player ,"coupe la",pc)
          pointsplayer=pointsplayer+1
     elif(player==tool[1] and pc==tool[2]):
         print("vous avez perdu le",pc,"coup la",player)
         pointspc=pointspc+1
     elif(player==tool[0] and pc==tool[2]):
         print("vous avez gagne la",player ,"ecrase le",pc)
         pointsplayer=pointsplayer+1
     else:
         print("vous ne pouvez jouer que soit pierre, feuille ou ciseaux.")
     player=input("rejouer : ")
     pc=(tool[randint(0,2)])
print("player: ",pointsplayer)
print("pc: ",pointspc)
if pointspc>pointsplayer:
   print("The winner is : pc")
else:

   print("The winner is : player")