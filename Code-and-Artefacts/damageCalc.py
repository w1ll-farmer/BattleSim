import random
from superEffective import superEffective
from ineffective import ineffective
from affect import affect
    #EFFECTIVENESS CHECKER
def effectiveCheck(attacker,defender,type,power,acc):
    effective=1 #all moves are assumed to be neutral
    types=[defender.type1,defender.type2] #for help when checking in a for loop later on
    for i in range(0,2):
        if superEffective(type,types[i])==True:
            effective=effective*2 #super effective moves have x2 multiplier
        elif ineffective(type,types[i])==True:
            effective=effective/2 #ineffective moves have x0.5 multiplier
        elif affect(type,types[i])==True:
            effective=0 #non-affecting moves have a x0 multiplier
    return effective

def damageCalc(defender,attacker,move):
    crit=False #default value
    moveNames=[attacker.move1,attacker.move2,attacker.move3,attacker.move4]
    moveTypes=[attacker.movetype1,attacker.movetype2,attacker.movetype3,attacker.movetype4]
    movePowers=[attacker.movepower1,attacker.movepower2,attacker.movepower3,attacker.movepower4]
    moveAccuracies=[attacker.moveaccuracy1,attacker.moveaccuracy2,attacker.moveaccuracy3,attacker.moveaccuracy4]
    movePhyses=[attacker.movephys1,attacker.movephys2,attacker.movephys3,attacker.movephys4]
    for i in range(0,4): #assigns user input to pokemon object move
        if move.lower()==moveNames[i].lower(): #matches right attributes for the calculation
            type=moveTypes[i]
            power=movePowers[i]
            acc=moveAccuracies[i]
            phys=movePhyses[i]
    if random.randint(1,8) ==8: #1 in 8 chance of getting a critical hit
        critical=1.5 #critical hit multiplier
        crit=True #ADDED STATEMENT
    else:
        critical=1
    randNum=(random.randint(88,100))/100 #generates a random 2-decimal-place number between 0.88 and 1
    if type == attacker.type1 or type == attacker.type2:
        STAB=1.5 #same type attack bonus multiplier is x1.5
    else:
        STAB=1
    effectiveness=effectiveCheck(attacker,defender,type,power,acc) #Checks how effective the move is
    modifier=STAB*randNum*critical*effectiveness
    if phys=='physical': #checks if move is physical
        attack=attacker.atk #uses physical attack and defence
        defensive=defender.defence
    else:
        attack=attacker.spAtk #otherwise uses special attack and defence
        defensive=defender.spDef
    #RETURNS DAMAGE
    return int(round((((((((2*attacker.level)/5)+2)*power*attack/defensive)/50)+2)*modifier),0)),crit, acc #returns the damage