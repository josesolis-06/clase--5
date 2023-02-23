import random

lista_nombres = ["Ithamar", "Leo", "Nacho", "Allan", "Jose", "Cris", "Carlos"]

random.shuffle(lista_nombres)


for indice, nombre in enumerate(lista_nombres):
    print(indice, nombre)


