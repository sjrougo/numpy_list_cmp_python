# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '-2', '3', '', '7', 'NaN']
    #lista = [x if(x % 2) == 0 else 0 for x in numeros]
    lista_numeros_enteros = [x if(x.isdigit()) == True else 0 for x in list_numeros_str]
    print(lista_numeros_enteros)

    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?

    '''Al cambiar uno de los valores a negativo, el método isdigit no lo toma como dígito, también lo probé 
    con números flotantes, y pasa igual así que entiendo que el método solo toma valores enteros positivos
    como dígitos. Es un punto a tener en cuenta al momento de usar dicho método'''

    print("terminamos")