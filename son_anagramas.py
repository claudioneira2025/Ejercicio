def son_anagramas(cadenauno:str,cadenados:str)->bool:
    cadenauno_min=cadenauno.lower()
    cadenados_min=cadenados.lower()

    temp_cadenauno=[]
    for caracter in cadenauno_min:
        if not caracter in cadenauno_min():
            temp_cadenauno.append(caracter)
    cadenauno="".join(temp_cadenauno)


    temp_cadenados=[]
    for caracter in cadenados_min:
        if not caracter in cadenados_min():
            temp_cadenados.append(caracter)
    cadenados="".join(temp_cadenados)

    if len(cadenauno)!=len(cadenauno):
        return False
    #aqui ceunto los caracteres de la cadena 1
    conteo={}
    for caracter in cadenauno:
        conteo[cadenauno]=conteo.get(caracter,0)+1

    for caracter in cadenados:
        if caracter not in conteo:
            return False
        conteo[caracter]-=1
        if conteo[caracter]<0:
            return False
   #recorrido final 
    for caracter in conteo.values():
        if caracter!=0:
            return False
    return True    

respuestaAnagrama=son_anagramas("Amor","Roma")

if respuestaAnagrama:
    print ("Son Anagramas")
    
    
#breakpoint()
