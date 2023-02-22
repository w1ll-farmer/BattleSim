def superEffective(atkType,defType):
    if atkType == 'Fire':
        if defType == 'Grass' or defType =='Ice' or defType =='Bug' or defType =='Steel':
            return True
    elif atkType == 'Water':
        if defType == 'Ground' or defType =='Fire' or defType =='Rock':
            return True
    elif atkType == 'Grass':
        if defType == 'Ground' or defType =='Rock' or defType =='Water':
            return True
    elif atkType == 'Rock':
        if defType == 'Flying' or defType =='Ice' or defType =='Bug' or defType =='Fire':
            return True
    elif atkType == 'Electric':
        if defType == 'Water' or defType =='Flying':
            return True
    elif atkType == 'Fighting':
        if defType == 'Rock' or defType =='Ice' or defType =='Normal' or defType =='Steel' or defType =='Dark':
            return True
    elif atkType == 'Psychic':
        if defType == 'Fighting' or defType =='Poison':
            return True
    elif atkType == 'Ghost':
        if defType == 'Psychic' or defType =='Ghost':
            return True
    elif atkType == 'Dark':
        if defType == 'Psychic' or defType =='Ghost':
            return True
    elif atkType == 'Ground':
        if defType == 'Fire' or defType =='Rock' or defType =='Electric' or defType =='Steel' or defType == 'Poison':
            return True
    elif atkType == 'Steel':
        if defType == 'Rock' or defType =='Ice' or defType =='Fairy':
            return True
    elif atkType == 'Poison':
        if defType == 'Grass':
            return True
    elif atkType == 'Flying':
        if defType == 'Grass' or defType =='Fighting' or defType =='Bug':
            return True
    elif atkType == 'Bug':
        if defType == 'Grass' or defType =='Psychic' or defType =='Dark':
            return True
    elif atkType == 'Ice':
        if defType == 'Grass' or defType == 'Ground' or defType == 'Dragon' or defType =='Flying':
            return True
    else:
        return False