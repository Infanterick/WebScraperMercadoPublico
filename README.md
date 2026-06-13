# Mercado Público - Web Scraping de Licitaciones Chile

Herramienta para descargar, procesar y filtrar licitaciones publicadas en el portal [Mercado Público de Chile](https://www.mercadopublico.cl/).

## Descripción

Este proyecto automatiza la recopilación de datos de licitaciones públicas disponibles en Mercado Público, permitiendo filtrar por región y palabras clave. Los resultados se exportan en un archivo Excel organizado por categorías para facilitar el análisis y seguimiento de oportunidades de negocio.

## Características

- ✅ Descarga automática de licitaciones desde Mercado Público
- ✅ Filtrado por región (defecto: Región del Maule)
- ✅ Búsqueda por palabras clave personalizables
- ✅ Generación de reportes en Excel con múltiples hojas
- ✅ Limpieza de datos (normalización de acentos, formatos de fecha)
- ✅ Registro detallado de operaciones (logs)
- ✅ Filtrado automático de licitaciones vigentes (fechas futuras)

## Requisitos

- Python 3.13+
- Las dependencias se encuentran en `pyproject.toml`

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Infanterick/MercadoPublico.git
cd MercadoPublico
```

### 2. Crear un entorno virtual (recomendado)

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -e .
```

O instalar las dependencias manualmente:
```bash
pip install pandas>=3.0.3 requests>=2.34.2 openpyxl>=3.1.5
```

## Uso

### Ejecución básica

```bash
python licitaciones.py
```

El script realizará las siguientes acciones:

1. Descarga el archivo de licitaciones desde Mercado Público
2. Descomprime y procesa los datos
3. Filtra licitaciones por región (Maule)
4. Muestra un cuadro de diálogo para ingresar palabras clave de filtrado
5. Genera un archivo Excel con los resultados

### Personalización

Dentro del script `licitaciones.py`, puedes modificar:

- **Región**: Cambia el filtro en la línea que contiene `"Maule"` para seleccionar otra región
- **Palabras clave por defecto**: Edita el parámetro `initialvalue` en la función `askstring()` (línea ~151)
- **URL de descarga**: Modifica la variable `url` (línea ~26) si es necesario

## Estructura del proyecto

```
MercadoPublico/
├── licitaciones.py          # Script principal
├── logger_config.py         # Configuración de logs
├── pyproject.toml          # Configuración de dependencias
├── README.md               # Este archivo
├── downloads/              # Carpeta para descargas (se crea automáticamente)
│   └── licitaciones/       # Archivos descomprimidos
└── log_file.log            # Archivo de registro de operaciones
```

## Archivos de salida

El script genera un archivo Excel con nombre: `licitaciones - DD-MM-YYYY - N.xlsx`

Dentro del archivo encontrarás:
- **Hoja "Maule"**: Todas las licitaciones de la región del Maule
- **Hojas adicionales**: Una por cada palabra clave ingresada, conteniendo licitaciones que coincidan con esa palabra

## Logs

Todas las operaciones se registran en `log_file.log` con el formato:
```
TIMESTAMP - LOGGER_NAME - NIVEL - MENSAJE
```

Niveles de registro: `INFO`, `ERROR`

## Funciones principales

### `descargar_y_descomprimir(url, destfile, exdir)`
Descarga el archivo ZIP desde Mercado Público y lo descomprime.

### `remove_accents(text)`
Normaliza el texto eliminando acentos para homogeneizar los datos.

### `manejo_datos()`
Orquesta el procesamiento completo: descarga, descompresión, limpieza y filtrado de datos.

### `guardar_excel(licitaciones, licitaciones_maule)`
Genera el archivo Excel con los resultados filtrados por palabras clave.

## Tratamiento de datos

El script realiza las siguientes transformaciones:

1. **Lectura**: Lee el archivo Excel omitiendo las primeras 7 filas
2. **Limpieza**: Elimina 4 columnas innecesarias
3. **Normalización**: Elimina acentos de encabezados
4. **Tipos de datos**: Convierte fechas y categorías al formato apropiado
5. **Filtrado**: Mantiene solo licitaciones con fecha de cierre en el futuro

## Solución de problemas

### El script no descarga datos
- Verifica tu conexión a internet
- Comprueba que la URL en `licitaciones.py` sea correcta
- Revisa el archivo `log_file.log` para más detalles

### Error al descomprimir
- El archivo ZIP podría estar corrupto
- Intenta eliminar la carpeta `downloads/` y ejecutar de nuevo

### Columnas inesperadas en el Excel
- Las columnas eliminadas pueden variar según actualizaciones de Mercado Público
- Ajusta los índices en la función `manejo_datos()` si es necesario

## Dependencias de desarrollo

Para desarrollo e integración continua:
```bash
pip install -e ".[dev]"
```

Incluye:
- `mypy`: Verificación de tipos
- `ruff`: Linter y formateador de código

## Notas importantes

- ⚠️ El script utiliza un cuadro de diálogo interactivo para ingresar palabras clave
- ⚠️ La región "Maule" está codificada; puedes cambiarla modificando el filtro
- ⚠️ Los datos se descargan cada vez que ejecutas el script

## Autor

**Erick Infante**  
Fecha de inicio: 30-05-2026

## Licencia

Este proyecto está disponible bajo licencia MIT.

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Contacto

Para preguntas o sugerencias, contacta a través de:
- Email: [infanterick1@gmail.com]

---

**Última actualización**: Junio 2024
