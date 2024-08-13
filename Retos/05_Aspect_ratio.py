"""

Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Url de ejemplo:
  https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
  imagen de 1920*1080px.

"""
import requests
from PIL import Image
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    response.raise_for_status()  # Esto lanza un error si la descarga falla
    return Image.open(BytesIO(response.content))

def calculate_aspect_ratio(image):
    width, height = image.size
    aspect_ratio = width / height
    return aspect_ratio

def main():
    url = input("Ingrese la URL de la imagen: ").strip()
    try:
        image = download_image(url)
        aspect_ratio = calculate_aspect_ratio(image)
        print(f"El aspect ratio de la imagen es: {aspect_ratio:.2f}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
    except IOError:
        print("Error al abrir la imagen. Asegúrate de que la URL es correcta y apunta a una imagen válida.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()
    