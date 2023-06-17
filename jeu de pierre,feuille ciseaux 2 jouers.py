print("jeux de piere,papier et ciseau.")
print("premier joueur a vous de jouer")
player1=input("premier joueur a vous: ")
tools=["pi","pa","ci"]
while(player1 not in tools):
    print("vous ne pouvez jouer que piere, papier ou ciseaux")
    player1=input("premier joueur a vous: ")

if player1== tools[0] or player1== tools[1] or player1== tools[2]:
    print("deuxiem jouer a vous.")
    player2=input("deuxieme jouer:")
    while(player2 not in tools):
      print("vous ne pouvez jouer que piere, papier ou ciseaux")
      player2=input("dexieme joueur a vous: ")

    if player1==player2:
        print("match nul.") 
    elif player1==tools[0] and player2==tools[1]:
     print("le dexieme jooeur a gagne.")
    elif player1==tools[0] and player2==tools[2]:
        print("le premiere joueur a gagne.")
    elif player1==tools[1] and player2==tools[0]:
        print("le premiere joueur a gagne.")
    elif player1==tools[1] and player2==tools[2]:
        print("le dexieme joueur a gagne.")
    elif player1==tools[2] and player2==tools[0]:
        print("le deuxieme joueur a gagne.")
    elif player1==tools[2] and player2==tools[1]:
        print("le premiere joueur a gagne.")
else :
    print("vous ne pouvez jouer que piere, papier ou ciseaux")
    










