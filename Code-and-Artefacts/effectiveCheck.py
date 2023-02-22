#EFFECTIVENESS CHECKER
def effectiveCheck(attacker,defender,type,power,acc,phys):
    effective=1 #all moves are assumed to be neutral
    types=[defender.type1,defender.type2] #for help when checking in a for loop later on
    for i in range(0,2):
        if superEffective(type,types[i])==True:
            effective=effective*2
        elif ineffective(type,types[i])==True:
            effective=effective/2
        elif affect(type,types[i])==True:
            effective=0
    return effective