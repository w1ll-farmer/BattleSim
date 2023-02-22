from damageCalc import damageCalc
from damageCalc import effectiveCheck
from random import randint
import pygame
from pygame.locals import *
global window
window=pygame.display.set_mode((1200,800))
def accuracyCheck(accuracy):
    if randint(1,100) > accuracy:
        return True
    else:
        return False

def fainted(pokemon):
    if pokemon.hp <=0:
        return True
    else:
        return False


def switch(opPok,userPok): #passes in all AI 'mon and current user 'mon
    quick=False #to be used to check if priority move is best option
    quickIdentity=['',''] #pokemon name, priority move name
    faintMoves=[] #list of moves that can KO user 'mon
    faintAccs=[] #list of accuracies of the faintMoves
    faintAttacker=[] #list of the pokemon who use the faintmoves
    highestDamage=0 #in case there are no moves that KO user 'mon
    highestDamageMove='' #name of highest damaging move
    highestDamageMon='' #name of pokemon with that move
    for i in range(0,6):
        if not fainted(opPok[i]):
            moves=[opPok[i].move1,opPok[i].move2,opPok[i].move3,opPok[i].move4]
            moveAccs=[opPok[i].moveaccuracy1,opPok[i].moveaccuracy2,opPok[i].moveaccuracy3,opPok[i].moveaccuracy4]
            for x in range(0,4): #checks damage of each move
                damage,crit,accuracy= damageCalc(userPok,opPok[i],moves[x])
                if damage >= userPok.hp: #checks if it can KO opponent
                    if moves[x] =='Quick Attack' or moves[x] == 'Extreme Speed':
                        quick=True #signifies that there is a priority move
                        quickIdentity=[opPok[i].name,moves[x]] #edited
                    else:
                        faintMoves.append(moves[x]) #moves that KO
                        faintAccs.append(moveAccs[x])
                        faintAttacker.append(opPok[i].name) #edited
                elif damage > highestDamage:
                    highestDamage=damage
                    highestDamageMove=moves[x] #to be used when no KO available
                    highestDamageMon=opPok[i].name #edited
        if quick == False and len(faintMoves) == 0:
            outMon=highestDamageMon
        elif quick==True:
            outMon=quickIdentity[0]
        else:
            highestAccuracyMove=''
            highestAccuracy=0
            highestAccuracyMon=''
            for i in range(0,len(faintMoves)):
                if faintAccs[i] > highestAccuracy:
                    highestAccuracy=faintAccs[i] #changed
                    highestAccuracyMove=faintMoves[i]
                    highestAccuracyMon=faintAttacker[i] #just added
            outMon=highestAccuracyMon
        for i in opPok:
            if i.name==outMon: #sets pokemon to send out
                x=i #x is the  other for loop index I use. given that i has been used already, i decided to use x for this
    return x


def artificial(outPok,opPok,userPok):
    faintMove=''
    faintAcc=0
    highestDamage=0
    highestDamageMove=''
    highestDamageAcc=0
    userDamage=0
    if fainted(outPok) == True:
        outPok = switch(opPok,userPok) #switches out a new pokemon
    outPok.drawOp(window, 900, 250) #displays new pokemon
    pygame.display.update()
    moves = [outPok.move1, outPok.move2, outPok.move3, outPok.move4]
    accs = [outPok.moveaccuracy1, outPok.moveaccuracy2, outPok.moveaccuracy3, outPok.moveaccuracy4]
    userMoves=[userPok.move1,userPok.move2,userPok.move3,userPok.move4]
    userDamage=[]
    for i in range(0,4):
        damage=damageCalc(userPok,outPok,moves[i])[0] #finds damage of each move
        if moves[i] =='Quick Attack' or moves[i] == 'Extreme Speed':
            priorityDamage=damage #priority moves that KO user are used 100% of time
        userDamage.append(damageCalc(outPok,userPok,userMoves[i])[0]) #added
        if userPok.hp < damage and accs[i] >= faintAcc: #new best move
            if faintMove != 'Quick Attack' and faintMove !='Extreme Speed':
                faintMove = moves[i]
                faintAcc = accs[i]
        elif highestDamage < damage: #if new damage is higher than old highest
            highestDamage = damage #set highest to new damage
            highestDamageMove=moves[i]
            highestDamageAcc=accs[i]
    miss=accuracyCheck(highestDamageAcc)
    priority=False
    for i in range(0,len(userDamage)):
        if userDamage[i] > outPok.hp and outPok.spd < userPok.spd:
            priority=True #if user can KO AI before it can move, use priority move
    if priority == True and ('Quick Attack' in moves or 'Extreme Speed' in moves):
        for x in range(0,4): #if any moves are priority
            if moves[x] =='Quick Attack' or moves[x] == 'Extreme Speed':
                priorityMove=moves[x] #use priority move
        return priorityMove,100,outPok #accuracy of priority moves always 100
    elif faintMove in moves: #if a move can cause user to faint, use it
        return faintMove,faintAcc,outPok
    else:
        return highestDamageMove,highestDamageAcc,outPok #use highest damaging





