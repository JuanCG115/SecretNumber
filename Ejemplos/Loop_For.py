lista = ['a','b','c','d']

for L in lista:
    numero_letra = lista.index(L) + 1
    print(f"Letra {numero_letra}: {L}")

lista2 = ['Paulo','Laura','Juan','Luis','Julia']

for nombre in lista2:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

for a,b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

dic = {'clave1':'a','vlave2':'b','clave3':'c'}

for item1,item2 in dic.items():
    print(item1,item2)