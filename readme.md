# Instalar Actualizaciones

sudo apt-get update

# Instalar mysql
sudo apt install mysql-server
sudo apt install mysql-client -y 
sudo apt install libmysqlclient-dev

en linux tanto mysql como mysqlclient requiren en el SO la libreria libmysqlclient-dev 
sudo apt-get install libmysqlclient-dev

# Crear usuario en MySQL
sudo mysql
CREATE USER 'js'@'localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES *.* TO 'js'@'localhost';
CREATE DATABASE bootcamp;

# Instalar Python
sudo apt install python3-pip
sudo apt install python3-venv -y
sudo apt install python3-dev -y
sudo apt install python3-wheel -y

# Crear entorno virtual
python3 -m venv env
pip install -r requirements.txt

# Para tener acceso se debe ejecutar de la siguiente manera
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Cuando sea https, se debe agregar la siguiente variable en settings
CSRF_TRUSTED_ORIGINS = ["https://cfmedical.run-us-west2.goorm.app"]


# Generar un Servicio en Linux
pip install unicorn  # es un puente que permite enlazar nginx con nuestra aplicacion

gunicorn --bind 0.0.0.0:8000 cf_medical.wsgi

si marca un error con la libreria de pymysql, se debe desactivar el entorno virtual e instalar fuera del entorno virtual como pip install pymysql  y tambien
pip install decode

## Creando el Sevicio en Linux
sudo vim etc/systemd/system/django.service
Agregar:

[Unit]
Description=Description
After=network.target

[Service]
User=js
Group=www-data
WorkingDirectory=/home/js/project/cf_medical
ExecStart=/home/js/project/cf_medical/env/bin/gunicorn --workers 3 --bind unix:cf_medical.sock cf_medical.wsgi

[Install]
WantedBy=multi-user.target

# Iniciar el Servicio creado
sudo systemctl start django

# Reiniciar el servicio cuando se reinicie el sistema
sudo systemctl enable django

# Instalar nginx
sudo apt-get install nginx -y

Generar un archivo
sudo vim /etc/nginx/sites-available/django
Agregar:

server {
    listen 80;
    server_name https://cfmedical.run-us-west2.goorm.app/;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/js/project/cf_medical/cf_medical.sock;
    }
}

# Indicar a nginx que vamos a usar nuestra configuracion
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/
comprobamos que todo este bien
sudo nginx -t

sudo systemctl restart nginx


# Habilitar Archivos Estaticos

Generar la carpeta static
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '45.55.40.115/static'
]

ejecutar:
python manage.py collectstatic 

# Congurar nginx para que reconozca los archivos estaticos
 sudo vim /etc/nginx/sites-available/django

Agregar:

 location /static/ {
    alias /home/js/project/cf_medical/staticfiles/;
 }

 sudo service django restart
 sudo service nginx restart



