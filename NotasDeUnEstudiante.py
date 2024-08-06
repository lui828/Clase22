nota1 = int(input("Ingresar nota1: "))
nota2 = int(input("Ingresar nota2: "))
nota3 = int(input("Ingresar nota3: "))
nota4 = int(input("Ingresar nota4: "))

media = ((nota1+nota2+nota3+nota4)/4)

if media >=90:
    print("A")
elif media >=80 and media <=89:
    print("B")
elif media>=70 and media <=79:
    print("C")
elif media <=60 and media>=69:
    print("D")
else:
    print("E")
    



