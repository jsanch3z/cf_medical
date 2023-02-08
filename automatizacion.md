# Automatizacion de Tareas
pip install fabric3

Verificamos los comando que tiene el archivo fabfile.py
fab -l  ó  fab --list

# Pasar argumentos, crea el forder por nombre example
fab mkdir:folder=example

fab --port=50519 -H 18.236.180.236 --user=js mkdir:folder=example


# Definir a que host nos queremos conectar
fab --port=50519 -H 18.236.180.236 --user=js deploy

# Definir la llave publica y otras variables para poder conectarnos automaticamente

```python
env.hosts = ['18.236.180.236']
env.port = '50519'
env.user = 'js'
env.key_filename = '/home/jesus/.ssh/id_ed25519.pub'
```
Probar conexion
```bash
$fab deploy
```


# Comando de forma local
```
$fab master:commit="Deploy con fabric en local"
```

