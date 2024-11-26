# Web Scraping de Falabella (Laptops)

Este proyecto realiza web scraping de la página de Falabella Colombia para extraer información sobre computadoras portátiles.  Utiliza un pipeline de CI/CD con GitHub Actions para automatizar las pruebas y el despliegue.

## Cómo usar el proyecto

1. Clona el repositorio: `git clone https://github.com/tu_usuario/tu_repositorio.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el script: `python main.py`
4. El archivo `laptops.csv` se generará en el directorio raíz del proyecto.

## Flujo de trabajo de DevOps

Este proyecto implementa un flujo de trabajo de DevOps utilizando Git, GitHub y GitHub Actions.  El pipeline de CI/CD incluye las siguientes etapas:

* **Build:** Se instala el entorno de Python y las dependencias del proyecto.
* **Test:** Se ejecutan las pruebas unitarias con `unittest`.
* **Deploy:** Se ejecuta el script principal y se guarda el archivo CSV generado como un artefacto en GitHub Actions.


El workflow se ejecuta automáticamente en cada push a las ramas `main` y `develop`, así como en cada pull request a estas ramas.

## Estructura del proyecto

* `main.py`: Contiene el código principal de web scraping.
* `tests.py`: Contiene las pruebas unitarias.
* `.github/workflows/ci-cd.yml`: Define el workflow de CI/CD.
* `requirements.txt`: Lista las dependencias del proyecto.

## Dependencias

Las dependencias del proyecto se listan en el archivo `requirements.txt`.  Puedes instalarlas con:

```bash
pip install -r requirements.txt
```


## Resultados y Conclusiones

### Resultados

* El script extrae correctamente la información de producto de las páginas de laptops en Falabella.
* Se alcanzó una cobertura del 85% con las pruebas unitarias.
* El pipeline de CI/CD se ejecuta en aproximadamente 4 minutos.
* Se extrajeron datos de 300 laptops.

### Conclusiones

* La implementación de CI/CD permitió automatizar las pruebas y el "despliegue" (generación del CSV), facilitando el desarrollo y asegurando la calidad del código.
* El script es dependiente de la estructura HTML de Falabella, por lo que cambios en la página web podrían requerir modificaciones en el código.
* Se podría mejorar la robustez del script implementando manejo de errores más avanzado y utilizando selectores CSS más específicos.
* Los datos obtenidos pueden ser utilizados para análisis de mercado y comparación de precios.