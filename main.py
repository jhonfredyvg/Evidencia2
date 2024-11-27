import os
from bs4 import BeautifulSoup
import requests
import pandas as pd
import logging
from tqdm import tqdm
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_falabella(url_base, num_pages=10):
    data = []
    try:
        for page in tqdm(range(1, num_pages + 1), desc="Procesando páginas"):
            url = f"{url_base}?page={page}"
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                html_content = response.content
                soup = BeautifulSoup(html_content, 'lxml')
                elements = soup.find_all('div', class_="jsx-1068418086")
                
                for element in elements:
                    try:
                        nombre_producto = element.find('b', class_='pod-subTitle').text.strip()
                        precio_texto = element.find('li', class_='prices-0').find('span', class_='copy10').text.strip()
                        precio = float(precio_texto.replace('$', '').replace('.', ''))
                        
                        data.append({
                            'Nombre': nombre_producto,
                            'Precio': precio,
                        })
                    except Exception as e:
                        logger.error(f"Error al procesar elemento: {e}")

            except requests.exceptions.RequestException as e:
                logger.error(f"Error al obtener la página {url}: {e}")
                break

        # Asegurar que existe la carpeta de datos
        os.makedirs('datos', exist_ok=True)

        # Generar CSV con timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        csv_filename = f"datos/laptops_{timestamp}.csv"
        
        # Crear DataFrame y guardar CSV
        df = pd.DataFrame(data)
        
        # Verificar si hay datos antes de guardar
        if not df.empty:
            df.to_csv(csv_filename, index=False)
            logger.info(f"Archivo CSV guardado: {csv_filename}")
            return df, csv_filename
        else:
            logger.warning("No se encontraron datos para scraping")
            return None, None

    except Exception as e:
        logger.error(f"Error general en scraping: {e}")
        return None, None

if __name__ == "__main__":
    url_base = 'https://www.falabella.com.co/falabella-co/category/cat1361001/Computadores-Portatiles'
    df, filename = scrape_falabella(url_base)
    if df is not None:
        print(df)
    else:
        print("No se pudo realizar el scraping")
        #Actualizar algun cambio en el archivo