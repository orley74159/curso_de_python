# lista en python
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)  # [1, 2, 3, 4, 5]
# Acceder a elementos de la lista
print(mi_lista[0])  # 1
print(mi_lista[2])  # 3
print(mi_lista[-1])  # 5
# Modificar elementos de la lista
mi_lista[1] = 20
print(mi_lista)  # [1, 20, 3, 4, 5]
# Agregar elementos a la lista
mi_lista.append(6)
print(mi_lista)  # [1, 20, 3, 4, 5, 6]
mi_lista.insert(2, 15)
print(mi_lista)  # [1, 20, 15, 3, 4, 5, 6]
# Eliminar elementos de la lista
mi_lista.remove(20)
print(mi_lista)  # [1, 15, 3, 4, 5, 6]
elemento_eliminado = mi_lista.pop(3)
print(elemento_eliminado)  # 4
print(mi_lista)  # [1, 15, 3, 5, 6]
# Funciones útiles con listas
print(len(mi_lista))  # Longitud de la lista
print(mi_lista.count(3))  # Cuenta cuántas veces aparece el elemento 3
print(mi_lista.index(5))  # Índice del elemento 5
# Listas anidadas
lista_anidada = [1, 2, [3, 4], 5]
print(lista_anidada[2])  # [3, 4]
print(lista_anidada[2][0])  # 3
print(lista_anidada[2][1])  # 4
# Convertir una tupla en una lista
mi_tupla = (10, 20, 30)
lista_desde_tupla = list(mi_tupla)
print(lista_desde_tupla)  # [10, 20, 30]
# Convertir una lista en una tupla
tupla_desde_lista = tuple(mi_lista)
print(tupla_desde_lista)  # (1, 15, 3, 5, 6)
# Iterar sobre una lista
for elemento in mi_lista:
    print(elemento)
# Verificar si un elemento está en una lista
print(3 in mi_lista)  # True
print(10 in mi_lista)  # False
# Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)  # [1, 2, 3,
# 4, 5, 6]
# Repetir listas
lista_repetida = lista1 * 3
print(lista_repetida)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# Slicing en listas
sub_lista = mi_lista[1:4]
print(sub_lista)  # [15, 3, 5]
# Listas con diferentes tipos de datos
lista_mixta = [1, "dos", 3.0, True]
print(lista_mixta)  # [1, 'dos', 3.0, True]
print(type(lista_mixta))  # <class 'list'>


# Funciones que retornan listas
def obtener_pares(valores):
    return [x for x in valores if x % 2 == 0]


resultado = obtener_pares([1, 2, 3, 4, 5, 6])
print(resultado)  # [2, 4, 6]
# Salida desempaquetada de funciones
pares = obtener_pares([1, 2, 3, 4, 5, 6])
print(pares)  # [2, 4, 6]
