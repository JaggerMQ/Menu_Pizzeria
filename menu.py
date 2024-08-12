print('***PIZZERIA PYTHON***')

print('---MENU---')
print('-Pizza de champiñones')
print('-Pizza cuatro quesos')
print('-Pizza de peperoni')

champiñones = 15.5
cuatro_quesos = 16.5
peperoni = 14.6

pizza = input('¿Que tipo de pizza desea elegir?: ')
if pizza == 'champiñones':
    print(f'Ha elegido la pizza de champiñones cuyo precio es de {champiñones}')
    efectivo = float(input('Ingrese un monto con el cual hacer la compra: '))

    ingrediente_precios = {
        'jamon': 2.5,
        'queso': 1.5,
        'tomate': 2.0,
        'tocineta': 2.5    
    }

    total = champiñones
    cambio = 0
    
    ingredientes = 'si'
    while ingredientes.lower() == 'si':
        print('Ingredientes disponibles: jamon, queso, tomate, tocineta')
        ingrediente = input('Ingrese el ingrediente que desea agregar: ')
        if ingrediente in ingrediente_precios:
            total += ingrediente_precios[ingrediente]
            print(f'Costo total acumulado: {total}')
            if total > efectivo:
                print('Tu total acumulado excede el monto de compra ingresado.')
                break
        else:
            print('Ingrediente no válido. Intente nuevamente.')

        ingredientes = input('¿Desea añadir algún ingrediente? (si/no): ')

    if total <= efectivo:
        cambio = efectivo - total
        print(f'Su pizza de champiñones con ingredientes adicionales tiene un precio total de: {total}')
        print('Puede retirar su pizza. ¡Gracias por su compra!')

    ticket = {
        'ticket': '---TICKET---',
        'pizza': f'Tipo de pizza: champiñones',
        'total': f'Precio total: {total}',
        'cambio': f'Cambio: {cambio}'
        }

    for valor in ticket.items():
        print(valor)

elif pizza == 'cuatro quesos':
    print(f'Ha elegido la pizza de cuatro quesos cuyo precio es de {cuatro_quesos}')
    efectivo = float(input('Ingrese un monto con el cual hacer la compra: '))

    ingrediente_precios = {
        'jamon': 2.5,
        'queso': 1.5,
        'tomate': 2.0,
        'tocineta': 2.5    
    }

    total = cuatro_quesos
    cambio = 0
    
    ingredientes = 'si'
    while ingredientes.lower() == 'si':
        print('Ingredientes disponibles: jamon, queso, tomate, tocineta')
        ingrediente = input('Ingrese el ingrediente que desea agregar: ')
        if ingrediente in ingrediente_precios:
            total += ingrediente_precios[ingrediente]
            print(f'Costo total acumulado: {total}')
            if total > efectivo:
                print('Tu total acumulado excede el monto de compra ingresado.')
                break
        else:
            print('Ingrediente no válido. Intente nuevamente.')

        ingredientes = input('¿Desea añadir algún ingrediente? (si/no): ')

    if total <= efectivo:
        cambio = efectivo - total
        print(f'Su pizza de champiñones con ingredientes adicionales tiene un precio total de: {total}')
        print('Puede retirar su pizza. ¡Gracias por su compra!')

    ticket = {
        'ticket': '---TICKET---',
        'pizza': f'Tipo de pizza: champiñones',
        'total': f'Precio total: {total}',
        'cambio': f'Cambio: {cambio}'
        }

    for valor in ticket.items():
        print(valor)

elif pizza == 'peperoni':
    print(f'Ha elegido la pizza de peperoni cuyo precio es de {peperoni}')
    efectivo = float(input('Ingrese un monto con el cual hacer la compra: '))

    ingrediente_precios = {
        'jamon': 2.5,
        'queso': 1.5,
        'tomate': 2.0,
        'tocineta': 2.5    
    }

    total = champiñones
    cambio = 0
    
    ingredientes = 'si'
    while ingredientes.lower() == 'si':
        print('Ingredientes disponibles: jamon, queso, tomate, tocineta')
        ingrediente = input('Ingrese el ingrediente que desea agregar: ')
        if ingrediente in ingrediente_precios:
            total += ingrediente_precios[ingrediente]
            print(f'Costo total acumulado: {total}')
            if total > efectivo:
                print('Tu total acumulado excede el monto de compra ingresado.')
                break
        else:
            print('Ingrediente no válido. Intente nuevamente.')

        ingredientes = input('¿Desea añadir algún ingrediente? (si/no): ')

    if total <= efectivo:
        cambio = efectivo - total
        print(f'Su pizza de champiñones con ingredientes adicionales tiene un precio total de: {total}')
        print('Puede retirar su pizza. ¡Gracias por su compra!')

    ticket = {
        'ticket': '---TICKET---',
        'pizza': f'Tipo de pizza: champiñones',
        'total': f'Precio total: {total}',
        'cambio': f'Cambio: {cambio}'
        }

    for valor in ticket.items():
        print(valor)

else:
    print('El tipo de pizza que solicita no esta disponible.')