def convertir_hora_24_a_12(hora_24):
    
    hora, minutos = map(int, hora_24.split(':'))
    
    if hora == 0:
        hora_12 = 12
        
    elif hora < 12:
        hora_12 = hora
        
    elif hora == 12:
        hora_12 = 12 
        sufijo = 'PM'
    else:
        hora_12 = hora - 12
        sufijo = 'PM'
        
        
    hora_12_formateada = f"{hora_12}:{minutos:02d}{sufijo}"
    
    return hora_12_formateada
hora_24 = "13:45"
hora_12 = convertir_hora_24_a_12(hora_24)
print(hora_12)

