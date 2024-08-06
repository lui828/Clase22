hora24 = input("Ingrese hora formato 24 horas(HH:MM):")
partes = hora24.split(":")
horas = int(partes[0])
minutos = int(partes[1])
doce = "am"
if horas>=12:
    doce = "pm"
if horas>12:
    horas-=12
elif horas==12:
    horas = 12
    print(f"la hora en formato de 12 es {horas}:{minutos:02d}{doce}")




