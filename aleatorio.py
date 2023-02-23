import random


lista = list(range(1, 11))

print(lista)

random.shuffle(lista)
print(lista)

aleatorio = random.randint(0, 10)
print(aleatorio)


listacarros = ["bmw", "audi", "toyota", "mercedes"]
marca_aleatoria = random.choice(listacarros)
print(marca_aleatoria)