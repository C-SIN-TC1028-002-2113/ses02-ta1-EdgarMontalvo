def main():
    #escribe tu código abajo de esta línea
    naci = float(input("Dame el año de nacimiento: "))
    año = float(input("Dame el año actual: "))
    lus = int(año-naci)/5
    print("Los lustros que has vivido son:", lus)

if __name__ == '__main__':
    main()
