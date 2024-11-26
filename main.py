import os
from bs4 import BeautifulSoup
import requests
import pandas as pd
import logging
from tqdm import tqdm
from datetime import datetime

# Disable DEBUG messages
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)

def scrape_falabella(url_base, num_pages=10):
    data = []
    for page in tqdm(range(1, num_pages + 1), desc="Procesando páginas"):
        url = f"{url_base}?page={page}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción si hay un error HTTP
            html_content = response.content
            soup = BeautifulSoup(html_content, 'lxml')
            elements = soup.find_all('div', class_="jsx-1068418086")
            for element in elements:
                try:  # Manejo de errores para elementos individuales
                    nombre_producto = element.find('b', class_='pod-subTitle').text.strip()
                    precio_texto = element.find('li', class_='prices-0').find('span', class_='copy10').text.strip()
                    precio = float(precio_texto.replace('$', '').replace('.', ''))
                    
                    data.append({
                        'Nombre': nombre_producto,
                        'Precio': precio,
                    })
                except Exception as e:
                    logging.error(f"Error al procesar elemento: {e}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Error al obtener la página {url}: {e}")
            break # Detener el scraping si hay un error de red

    # Asegurar que existe la carpeta de datos si no existe
    os.makedirs('datos', exist_ok=True)

    # Generar CSV con timestamp en la carpeta 'datos'
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    csv_filename = f"datos/laptops_{timestamp}.csv"
    
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False)
    
    print(f"Archivo CSV guardado: {csv_filename}")
    return df

if __name__ == "__main__":
    url_base = 'https://www.falabella.com.co/falabella-co/category/cat1361001/Computadores-Portatiles'
    df = scrape_falabella(url_base)
    print(df)