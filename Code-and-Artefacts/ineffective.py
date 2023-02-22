def ineffective(atkType,defType):
    if atkType == 'Fire':
        if defType == 'Water' or defType == 'Rock' or defType =='Fire' or defType=='Dragon':
            return True
    elif atkType == 'Steel':
        if defType =='Water' or defType =='Fire' or defType =='Steel' or defType =='Electric':
            return True
    elif atkType == 'Water':
        if defType =='Water' or defType =='Grass' or defType =='Dragon':
            return True
    elif atkType =='Grass':
        if defType == 'Fire' or defType == 'Grass' or defType =='Steel' or defType=='Poison' or defType=='Flying' or defType =='Bug' or defType =='Dragon':
            return True
    elif atkType == 'Normal':
        if defType =='Rock' or defType =='Steel':
            return True
    elif atkType == 'Fighting':
        if defType =='Flying' or defType =='Psychic' or defType =='Poison' or defType =='Bug':
            return True
    elif atkType == 'Electric':
        if defType =='Grass' or defType =='Electric' or defType =='Dragon':
            return True
    elif atkType == 'Ice':
        if defType =='Water' or defType =='Fire' or defType =='Steel' or defType =='Ice':
            return True
    elif atkType == 'Poison':
        if defType =='Ground' or defType =='Poison' or defType =='Rock' or defType =='Ghost':
            return True
    elif atkType == 'Ground':
        if defType =='Grass' or defType =='Bug':
            return True
    elif atkType == 'Flying':
        if defType =='Rock' or defType =='Steel' or defType =='Electric':
            return True
    elif atkType == 'Psychic':
        if defType =='Psychic' or defType =='Steel':
            return True
    elif atkType == 'Bug':
        if defType =='Poison' or defType =='Fire' or defType =='Steel' or defType =='Fighting' or defType=='Flying' or defType=='Ghost':
            return True
    elif atkType == 'Rock':
        if defType =='Fighting' or defType =='Ground' or defType =='Steel':
            return True
    elif atkType == 'Ghost':
        if defType =='Dark':
            return True
    elif atkType == 'Dragon':
        if defType =='Steel':
            return True
    elif atkType == 'Dark':
        if defType =='Fighting' or defType =='Dark':
            return True
    else:
        return False