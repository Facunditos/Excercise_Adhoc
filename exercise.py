lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25)
]


def ordenar(lista_personas):
    """ El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    lista_edades_ordenadas=[]
    for x in range(len(lista_personas)):
        lista_edades_ordenadas.append(lista_personas[x][3])   
    lista_edades_ordenadas.sort()
    return lista_edades_ordenadas
    pass

def convertir_a_diccionario(lista_personas):
    """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
    diccionario={lista_personas[x][0]:lista_personas[x][1:] for x in range(len(lista_personas))}
    return diccionario

    pass


def devolver_edad(lista_personas, dni):
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    diccionario=convertir_a_diccionario(lista_personas)
    for clave,valor in diccionario.items():
        if clave==dni:
            edad=valor[2]
        else:
            edad='no encontramos a esa persona, prueba con otro D.N.I'
    return edad
    
    pass


def eliminar_repetidos(lista_personas):
    """ El metodo debe devolver los elementos unicos """
    lista_personas_no_repetidas=[]
    for x in range(len(lista_personas)):
        if lista_personas[x] not in lista_personas_no_repetidas:
            lista_personas_no_repetidas.append(lista_personas[x])
    return lista_personas_no_repetidas
    pass


def separar_por_edad(lista_personas):
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    lista_mayoresOiguales_25=[]
    lista_menores_25=[]
    for x in range(len(lista_personas)):
        if lista_personas[x][3]>=25:
            lista_mayoresOiguales_25.append(lista_personas[x])
        else:
            lista_menores_25.append(lista_personas[x])
    return lista_mayoresOiguales_25,lista_menores_25


def obtener_promedio(lista):
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    try:
        return sum(lista)/len(lista)
    except ZeroDivisionError:
        return 'no se puede obtener el promedio de una lista vacía, pues no es posible dividir por cero'
    pass


def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))

main()
