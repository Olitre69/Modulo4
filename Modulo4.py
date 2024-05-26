import os  # Importar el módulo os para interactuar con el sistema operativo
import requests  # Importar la biblioteca requests para realizar solicitudes HTTP
import json  # Importar el módulo json para manipular datos JSON

def obtener_datos_pokemon(nombre_pokemon):
    """
    Función para obtener los datos de un Pokémon desde la API de Pokémon.

    Args:
        nombre_pokemon (str): El nombre del Pokémon a buscar.

    Returns:
        dict: Los datos del Pokémon en formato JSON si se encuentra, None si no se encuentra.
    """
    # Construir la URL para consultar la API de Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    
    # Realizar la solicitud GET a la API
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        data = response.json()
        return data
    else:
        # Mostrar mensaje de error si el Pokémon no fue encontrado
        print("¡Error! Pokémon no encontrado.")
        return None

def mostrar_informacion_pokemon(data):
    """
    Función para mostrar la información de un Pokémon y guardarla en un archivo JSON.

    Args:
        data (dict): Los datos del Pokémon en formato JSON.
    """
    # Mostrar información del Pokémon
    print("Nombre:", data['name'].capitalize())
    print("Peso:", data['weight'])
    print("Altura:", data['height'])
    print("Tipos:")
    for tipo in data['types']:
        print("-", tipo['type']['name'].capitalize())
    print("Habilidades:")
    for habilidad in data['abilities']:
        print("-", habilidad['ability']['name'].capitalize())
    print("Movimientos:")
    for movimiento in data['moves'][:5]:  # Mostrar solo los primeros 5 movimientos
        print("-", movimiento['move']['name'].capitalize())

    # Obtener URL de la imagen frontal del Pokémon
    image_url = data['sprites']['front_default']
    if image_url:
        # Abrir la imagen en el navegador web
        os.system(f"start {image_url}")

    # Guardar la información del Pokémon en un archivo JSON
    with open(f"pokedex/{data['name']}.json", 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # Solicitar al usuario que introduzca el nombre del Pokémon
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    
    # Obtener los datos del Pokémon desde la API
    pokemon_data = obtener_datos_pokemon(nombre_pokemon)
    
    # Verificar si se encontraron datos del Pokémon
    if pokemon_data:
        # Mostrar la información del Pokémon
        mostrar_informacion_pokemon(pokemon_data)

if __name__ == "__main__":
    # Verificar si la carpeta "pokedex" existe, si no, crearla
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
    
    # Ejecutar la función principal
    main()
