# Web Scraping de Falabella (Laptops)

Este proyecto realiza web scraping de la página de Falabella Colombia para extraer información sobre computadoras portátiles.  Utiliza un pipeline de CI/CD con GitHub Actions para automatizar las pruebas, la ejecución del scraping y la subida de los datos.

## Cómo usar el proyecto

1. Clona el repositorio: `git clone https://github.com/tu_usuario/tu_repositorio.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el script: `python main.py`
4. Los archivos CSV generados se guardarán en la carpeta `datos`, con nombres que incluyen un timestamp.


## Flujo de trabajo de DevOps

Este proyecto implementa un flujo de trabajo de DevOps utilizando Git, GitHub y GitHub Actions.  El pipeline de CI/CD incluye las siguientes etapas:

* **Build:** Se instala el entorno de Python y las dependencias del proyecto.
* **Test:** Se ejecutan las pruebas unitarias (si existen).
* **Deploy (solo en rama `main`):** Se ejecuta el script principal (`main.py`), se busca el archivo CSV generado más reciente, se agrega al repositorio, se crea un commit y se sube (push) a la rama `main`. El CSV también se guarda como un artefacto descargable en GitHub Actions.

El workflow se ejecuta automáticamente en cada push a las ramas `main` y `Rama1`, así como en cada pull request a estas ramas.

## Estructura del proyecto

* `main.py`: Contiene el código principal de web scraping.
* `tests.py`: Contiene las pruebas unitarias (si existen).
* `.github/workflows/ci-cd.yml`: Define el workflow de CI/CD.
* `requirements.txt`: Lista las dependencias del proyecto.
* `datos/`: Carpeta donde se guardan los archivos CSV generados.


## Dependencias

Las dependencias del proyecto se listan en el archivo `requirements.txt`.  Puedes instalarlas con:

```bash
pip install -r requirements.txt