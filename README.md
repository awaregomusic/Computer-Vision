# Proyecto: Computer Vision — Análisis Facial con DeepFace

Análisis automático de rostros en imágenes usando DeepFace. El proyecto detecta rostros, estima edad, género y emoción dominante, verifica si dos imágenes corresponden a la misma persona, y dibuja bounding boxes sobre los rostros detectados.

---

## Requisitos previos

- Python 3.9 o superior
- Git

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/awaregomusic/Computer-Vision.git
cd Computer-Vision
```

### 2. Crear entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Uso

Abre el notebook principal en Jupyter:

```bash
jupyter notebook analisis_facial.ipynb
```

Ejecuta las celdas en orden. El notebook descarga automáticamente imágenes de muestra en la carpeta `img/` al correr por primera vez.

---

## Contenido del notebook

| Sección | Descripción |
|---|---|
| 1. Descarga de imágenes | Obtiene imágenes de rostros de dominio público |
| 2. Visualización | Muestra las imágenes cargadas |
| 3. Análisis facial | Detecta emoción, edad y género con DeepFace |
| 4. Gráfica de emociones | Barras horizontales con probabilidades por emoción |
| 5. Verificación de identidad | Compara pares de imágenes y determina si es la misma persona |
| 6. Detección con bounding boxes | Dibuja los rectángulos sobre los rostros detectados |

---

## Estructura del proyecto

```
Computer-Vision/
├── analisis_facial.ipynb   # Notebook principal
├── requirements.txt        # Dependencias
├── README.md               # Este archivo
└── img/                    # Imágenes (se genera automáticamente)
```
