def affect(atkType,defType):
    if atkType == 'Ghost' and defType =='Normal':
        return True
    elif atkType =='Normal' and defType=='Ghost':
        return True
    elif atkType =='Fighting' and defType=='Ghost':
        return True
    elif atkType=='Poison' and defType=='Steel':
        return True
    elif atkType=='Ground' and defType=='Flying':
        return True
    elif atkType=='Electric' and defType=='Ground':
        return True
    elif atkType=='Psychic' and defType=='Dark':
        return True
    else:
        return False