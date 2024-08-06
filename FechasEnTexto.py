def convertir_fecha(fecha):
    
    meses = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6,
        'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
    
    partes = fecha.split()
    
    dia = int(partes[0].strip(','))
    mes = meses[partes[1]]
    año = int(partes[2])
    
    print(dia, mes, año)

fecha = "15, Febrero 1989"
convertir_fecha(fecha)
