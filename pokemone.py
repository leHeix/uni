genero = None

while genero != "hombre" and genero != "mujer":
    genero = input("Eres hombre o mujer? ")

print(f"bienvenid{"a" if genero == "mujer" else "o"} al mundo pokemon")

edad = None

while edad == None:
    edad_str = input("Introduce tu edad: ")
    try:
        edad = int(edad_str)
    except ValueError:
        print("Debes introducir un número como tu edad.")

if edad < 10:
    print(f"No tienes edad para ser un{"a entrenadora" if genero == "mujer" else " entrenador"}")
    quit()

print("Selecciona tu pokémon preferido con el número indicado:")
print("* 1 - Charmander")
print("* 2 - Bulbasaur")
print("* 3 - Squirtle")

pokemon_seleccionado = None

while pokemon_seleccionado == None:
    pokemon_seleccionado_str = input("=> ")
    try:
        pokemon_seleccionado = int(pokemon_seleccionado_str)
        if pokemon_seleccionado < 1 or pokemon_seleccionado > 3:
            raise Exception()
    except:
        print("Ese no es un pokémon válido")
        pokemon_seleccionado = None

pokemones = ["charmander", "bulbasaur", "squirtle"]
print(f"Bien! Tu pokémon es: {pokemones[pokemon_seleccionado - 1]}")

print("Selecciona tu región preferida con el número indicado:")
print("* 1 - Kanto")
print("* 2 - Hoenn")
print("* 3 - Johto")

region_seleccionada = None

while region_seleccionada == None:
    region_seleccionada_str = input("=> ")
    try:
        region_seleccionada = int(region_seleccionada_str)
        if region_seleccionada < 1 or region_seleccionada > 3:
            raise Exception()
    except:
        print("Esa no es una región válida")
        region_seleccionada = None

regiones = ["Kanto", "Hoenn", "Johto"]
print(f"Bien! Tu región es: {regiones[region_seleccionada - 1]}")
