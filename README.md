# Sistema de Asistencia con Reconocimiento Facial

Detecta y registra automáticamente la asistencia de personas reconociendo sus rostros en tiempo real desde la cámara. Guarda un CSV por día en `attendance/`.

---

## Requisitos previos

- Python 3.9+
- CMake instalado en el sistema ([cmake.org](https://cmake.org/download/))
- Cámara web

---

## Instalación

```bash
git clone https://github.com/awaregomusic/Computer-Vision.git
cd Computer-Vision
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## Uso

### 1. Registrar personas

Ejecuta una vez por cada persona. Apunta la cámara al rostro y presiona **ESPACIO** para capturar.

```bash
python register.py
```

Las fotos se guardan en `known_faces/{nombre}.jpg`.

### 2. Iniciar el sistema de asistencia

```bash
python attendance.py
```

- Detecta rostros en tiempo real.
- Cuando reconoce a alguien, registra nombre y hora en `attendance/YYYY-MM-DD.csv`.
- Cada persona se registra **una sola vez por día**.
- Verde = reconocido, Rojo = desconocido.
- Presiona **Q** para salir.

---

## Estructura

```
Computer-Vision/
├── register.py       # Registrar una persona nueva
├── attendance.py     # Sistema de asistencia en tiempo real
├── requirements.txt
├── README.md
├── known_faces/      # Fotos de personas registradas (se crea automáticamente)
└── attendance/       # CSVs de asistencia por día (se crea automáticamente)
```
