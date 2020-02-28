
# Esta funcion es la de arranque y se llama en el final del archivo 
def init():
    run = True
    print('\n********* init arranca *********')
    print('Bienvendio a la calculadora con funciones')
    while run:
        print('1 Suma')
        print('2 Multiplica')
        print('3 Salir')
        selected = input('\nSeleccione una opcion: ')

        if selected == '1':
            suma()
        elif selected == '2':
            numX = int(input('Ingrese el primer numero: '))
            numY = int(input('Ingrese el segundo numero: '))
            multiplica(numX, numY)
        else:
            print('Cerrando el programa')
            run = False

    

# se declara funcion suma, no recibe argumentos
def suma():
    # el input se pone dentro de int() para que el sistema automaticamente convierta lo que ingreses a un numero que puedas operar
    # ya que no puedes realizar una suma entre dos cadenas de texto
    numX = int(input('Ingrese el primer numero: '))
    numY = int(input('Ingrese el segundo numero: '))

    print('\n********* resultado de la suma funcion *********')
    print('El resultado de la suma es: ', numX + numX, '\n')

# se declara funcion con argumentos
def multiplica(numX, numY):
    print('\n********* resultado multiplicacion *********')
    print('El resultado de la multiplicacion es: ', numX * numY, '\n')
    

# Aqui es donde arranca el programa, el metodo de arranque si o si debe estar al final
init()


