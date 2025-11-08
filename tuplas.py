# Las listas son datos que pueden cambiar, las tuplas son datos que no pueden cambiar
# Las tuplas se representan con paréntesis ()
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
print(type(mi_tupla))
# Acceder a los elementos de una tupla
print(mi_tupla[0])  # Primer elemento
print(mi_tupla[2])  # Tercer elemento

# Las tuplas son inmutables, no se pueden modificar
# mi_tupla[0] = 10  # Esto generará un error
# Sin embargo, se pueden realizar operaciones que generen nuevas tuplas
nueva_tupla = mi_tupla + (6, 7, 8)
print(nueva_tupla)
# Desempaquetado de tuplas
a, b, c, d, e = mi_tupla
print(a)  # 1
print(b)  # 2

# Funciones útiles con tuplas
print(len(mi_tupla))  # Longitud de la tupla
print(mi_tupla.count(2))  # Cuenta cuántas veces aparece el elemento 2
print(mi_tupla.index(3))  # Índice del elemento 3

# Tuplas anidadas
tupla_anidada = (1, 2, (3, 4), 5)
print(tupla_anidada[2])  # (3, 4)

print(tupla_anidada[2][0])  # 3
print(tupla_anidada[2][1])  # 4
# Convertir una lista en una tupla
mi_lista = [10, 20, 30]
tupla_desde_lista = tuple(mi_lista)
print(tupla_desde_lista)  # (10, 20, 30)
# Convertir una tupla en una lista
lista_desde_tupla = list(mi_tupla)
print(lista_desde_tupla)  # [1, 2, 3, 4, 5]
# Tuplas con un solo elemento
tupla_un_elemento = (42,)
print(type(tupla_un_elemento))  # <class 'tuple'>
tupla_no_es_tupla = 42
print(type(tupla_no_es_tupla))  # <class 'int'>
# Iterar sobre una tupla
for elemento in mi_tupla:
    print(elemento)
# Verificar si un elemento está en una tupla
print(3 in mi_tupla)  # True
print(10 in mi_tupla)  # False
# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # (1, 2, 3, 4, 5, 6)
# Repetir tuplas
tupla_repetida = tupla1 * 3
print(tupla_repetida)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# Slicing en tuplas
sub_tupla = mi_tupla[1:4]
print(sub_tupla)  # (2, 3, 4)
# Tuplas con diferentes tipos de datos
tupla_mixta = (1, "dos", 3.0, True)
print(tupla_mixta)  # (1, 'dos', 3.0, True)
print(type(tupla_mixta))  # <class 'tuple'>


# Funciones que retornan tuplas
def min_max(valores):
    return (min(valores), max(valores))


resultado = min_max([3, 1, 4, 1, 5, 9])
print(resultado)  # (1, 9)
# Salida desempaquetada de funciones
min_val, max_val = min_max([3, 1, 4, 1, 5, 9])
print(min_val)  # 1
print(max_val)  # 9
# Tuplas como claves en diccionarios
mi_diccionario = {(1, 2): "valor1", (3, 4): "valor2"}
print(mi_diccionario[(1, 2)])  # valor1
print(mi_diccionario[(3, 4)])  # valor2
# Comparación de tuplas
tupla_a = (1, 2, 3)
tupla_b = (1, 2, 4)
print(tupla_a < tupla_b)  # True
print(tupla_a == tupla_b)  # False
# Funciones integradas con tuplas
print(sorted(mi_tupla))  # [1, 2, 3, 4, 5]
print(reversed(mi_tupla))  # <reversed object>
print(tuple(reversed(mi_tupla)))  # (5, 4, 3, 2, 1)
# Empaquetado y desempaquetado avanzado
tupla_varios = 1, 2, 3, 4, 5
print(tupla_varios)  # (1, 2, 3, 4, 5)
x, *y, z = tupla_varios
print(x)  # 1
print(y)  # [2, 3, 4]
print(z)  # 5
# Uso de tuplas en bucles con enumerate
for indice, valor in enumerate(mi_tupla):
    print(f"Índice: {indice}, Valor: {valor}")
# Salida:
# Índice: 0, Valor: 1
# Índice: 1, Valor: 2
# Índice: 2, Valor: 3
# Índice: 3, Valor: 4
# Índice: 4, Valor: 5
# Funciones zip con tuplas
tupla_numeros = (1, 2, 3)
tupla_letras = ("a", "b", "c")
combinado = zip(tupla_numeros, tupla_letras)
print(list(combinado))  # [(1, 'a'), (2, 'b'), (3, 'c')]


# Uso de tuplas para retornar múltiples valores en funciones
def operaciones(a, b):
    suma = a + b
    producto = a * b
    return suma, producto


resultado = operaciones(3, 4)
print(resultado)  # (7, 12)
suma, producto = operaciones(3, 4)
print(suma)  # 7
print(producto)  # 12
# Tuplas y memoria
import sys

tupla_grande = tuple(range(1000))
lista_grande = list(range(1000))
print(sys.getsizeof(tupla_grande))  # Tamaño en bytes de la tu
print(sys.getsizeof(lista_grande))  # Tamaño en bytes de la lista
# Salida:
# 8056
# 9024
tupla_grande = tuple(range(100000))
print(sys.getsizeof(tupla_grande))  # Tamaño en bytes de la tupla grande
# Salida:
# 800056
