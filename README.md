# Proyecto página web de hoteleria
## Instrucciones de Instalación

1. **Clonar Repositorio:** https://github.com/nmarchantp/Seihitsu_hotel.git
2. **Crear Entorno Virtual:**
  ```
python -m venv myvenv
  ```   
3. **Activar Entorno Virtual:**
  ```
myvenv\Scripts\activate
  ```  
4. **Instalar Django con requirements.txt:**
  ```
pip install -r requirements.txt
  ```  
5. **Configurar Base de Datos:**
   La base de datos incluye las tablas de Django por defecto cargadas.
  - Ejecutar migraciones:
  ```
python manage.py makemigrations web utilidades hoteles eventos servicios usuarios clientes reservas reportes
python manage.py migrate
  ```
6. **Cargar Datos Iniciales:**
   ```
python load_data.py
   ``` 
7. **Ejecutar el Servidor de Desarrollo:**
   ```
python manage.py runserver
   ``` 
8. **Acceso al Superusuario:**
  - El superusuario se crea con el archivo `load_data.py`.
  - Credenciales: Usuario: `nikoo`, Contraseña: `nikoo123`

