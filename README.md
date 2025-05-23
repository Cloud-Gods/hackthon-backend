# 📘 Proyecto CRUD de Usuarios con FastAPI y PostgreSQL

Este proyecto es una API básica para la gestión de usuarios utilizando **FastAPI** y **PostgreSQL**. Está organizada con una estructura modular para facilitar su mantenimiento y escalabilidad.

---

## 🛠️ Requisitos previos

Asegúrate de tener instalado:

- Python 3.10 o superior
- PostgreSQL
- Git
- virtualenv

---

## 🚀 Pasos para ejecutar el proyecto

### 1. Clonar el repositorio (opcional)

```bash
git clone https://github.com/AlejandroBecerraAcevedo/hackanthon-cloudgod.git
cd hackanthon-cloudgod
```

### 2. Crear y activar un entorno virtual
En Windows:

```bash
python -m venv env
.\env\Scripts\activate
```

En Linux / macOS:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear el archivo .env
Crea un archivo llamado .env en la raíz del proyecto con este contenido:

```bash
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/mi_basededatos
```

### 5. Crear la base de datos en PostgreSQL

```bash
CREATE DATABASE mi_basededatos;
```

### 6. Levantar el servidor de desarrollo

```bash
uvicorn app.main:app --reload
```

### 7. Documentación en Swagger

```bash
http://127.0.0.1:8000/docs
```

🧪 Endpoints disponibles

-> GET /users/ → Obtener todos los usuarios

-> GET /users/{id} → Obtener un usuario por ID

-> POST /users/ → Crear un nuevo usuario

-> DELETE /users/{id} → Eliminar un usuario



📂 Estructura del Proyecto

```
project_root/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── controllers/
│   ├── services/
│   ├── routers/
│   ├── schemas/
│   └── utils/
├── .env
├── requirements.txt
└── README.md
```

📄 Licencia
Este proyecto es de código abierto bajo la licencia MIT.