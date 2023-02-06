# Instalar Actualizaciones

sudo apt-get update

# Instalar mysql
sudo apt install mysql-server
sudo apt install mysql-client -y 
sudo apt install libmysqlclient-dev

# Crear usuario en MySQL
sudo mysql
CREATE USER 'js'@'localhost IDENTIFIED BY 'js';
GRANT ALL PRIVILEGES *.* TO 'js'@'localhost';
CREATE DATABASE bootcamp;

