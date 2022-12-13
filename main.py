def main():
    ingreso = input('Escriba su lista de paises, separados por una coma:')
    listapaises = ingreso.split(',')
    nuevalista = []
    for lista in listapaises:
        a = lista.strip().capitalize()
        nuevalista.append(a)

    nuevalista = set(nuevalista)
    print(f'{sorted(nuevalista)} y cantidad: {len(nuevalista)}')



if __name__ == '__main__':
    main()