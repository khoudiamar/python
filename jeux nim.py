Python 2.7.15rc1 (v2.7.15rc1:bad9a580ca, Apr 14 2018, 23:30:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random as h
import math as m
def nvTas():
    return [h.randrange(5,24) for i in range(h.randrange(3,8))]
def calculScore(tour):
    tot=0
    for i in range(m.ceil(tour/2)): 
        tot+=i*(10**i)
    return tot
    
def affichTop10():
    print("Top 10:")
    scoreList=[]
    index=0
    listrange=0
  
    with open("fich.txt",'r') as save:
        for best in save:
            scoreList.append([best.strip('\n').split(':')[0],best.strip('\n').split(':')[2]])
    if len(scoreList) <10:
        listrange=len(scoreList)
    else:
        listrange=10
    for l in range(listrange):
        index=0
        maximum=int(scoreList[0][1])
        for i in range(len(scoreList)):
            if int(scoreList[i][1])>maximum:
                maximum=int(scoreList[i][1])
                index=i 
        print(l+1,".",scoreList[index][0],":",maximum)
        scoreList.remove(scoreList[index])
             
            
    
def st():
    global nomJoueur1
    global nomJoueur2
    global ancienScore1
    global ancienScore2
    global bestScore1
    global bestScore2
    
    
    nomJoueur1,nomJoueur2=("choisir","choisir")
    ancienScore1,bestScore1,ancienScore2,bestScore2=0,0,0,0
    joueur1=input(" entrez votre nom1: ")
    joueur2=input("entrez votre nom2: ")
    with open("fich.txt",'r') as save:
        for ligne in save:
            if ligne.split(':')[0]==joueur1:
                nomJoueur1,ancienScore1,bestScore1=ligne.strip('\n').split(':')
                
            if ligne.split(':')[0]==joueur2:
                nomJoueur2,ancienScore2,bestScore2=ligne.strip('\n').split(':')
                
    if nomJoueur1=="choisir":
        nomJoueur1=joueur1
    if nomJoueur2=="choisir":
        nomJoueur2=joueur2
    
def affi(tas):
    string=""
    for i in range(len(tas)):
        string+=str(i+1)+"|"
        for piece in range(tas[i]):
            string+="*"
        for espace in range(23-tas[i]):
            string+=" "
        print(string,"| ",tas[i])
        string=""
def nbrPieceTotal(tas):
    total=0
    for i in tas:
        total+=i
    return total
def jouer():
    tas=nvTas()
    st()
    print("Joueur1:",nomJoueur1,"| Score partie précédente:",ancienScore1,"| Meilleur Score:",bestScore1)
    print("Joueur2:",nomJoueur2,"| Score partie précédente:",ancienScore2,"| Meilleur Score:",bestScore2)
    tour=1
    while True:
        if tour%2==0:
            print("le tour de",nomJoueur2)
        else:
            print("le tour de",nomJoueur1)
        
        affi(tas)
        print("Choisir un tas: ")
        numTas=int(input())
        print("Choisissez un nombre de pieces: ")
        nbrPiece=int(input())
        try:
            if tas[numTas-1] or tas[numTas-1]<=0:
                if nbrPiece<=23 and nbrPiece>0:
                    if nbrPieceTotal(tas)-nbrPiece <1:
                        score=calculScore(tour)
                        f = open("fich.txt","r")
                        lignes = f.readlines()
                        f.close()
                        if tour%2==0:
                            print(nomJoueur1," partie gagnie le score est:",score)
                            
                            with open("fich.txt",'w') as fich:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJoueur1:
                                            pass
                                        else:
                                            fich.write(ligne)
                            with open("fich.txt",'a') as save:
                                
                                if score>int(bestScore1):
                                    fich.write("{}:{}:{}\n".format(nomJoueur1,score,score))
                                else:
                                    fich.write("{}:{}:{}\n".format(nomJoueur1,score,bestScore1))

                        else:
                            print(nomJoueur2," partie gagnie  le score:",score)
                            with open("fich.txt",'w') as fich:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJoueur2:
                                            pass
                                        else:
                                            fich.write(ligne)
                            with open("fich.txt",'a') as fich:
                                if score>int(bestScore1):
                                    fich.write("{}:{}:{}\n".format(nomJoueur2,score,score))
                                else:
                                    fich.write("{}:{}:{}\n".format(nomJoueur2,score,bestScore2))
                        print("jeux terminer")
                        affichTop10()
                        break  
                
                    if tas[numTas-1]-nbrPiece >=0:
                        tas[numTas-1]-=nbrPiece
                        tour+=1
                else:
                    print("Choix du nombre de pieces incorrect")
            else:
                print("Choix du tas incorrect")
        except:
            print("Il y a eu une erreur  réessayer")
    nouvPartie=input("Voulez vous lancer une nouvelle partie? oui/non  ")
    if nouvPartie=="oui":
        jouer()
    else:
        print("jeux terminer")
        
jouer()	
