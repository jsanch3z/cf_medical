from fabric.api import run
from fabric.api import env, cd, prefix, sudo
from fabric.api import local

env.hosts = ['18.236.180.236']
env.port = '50519'
env.user = 'js'
env.key_filename = '/home/jesus/.ssh/id_ed25519.pub'

def hello_world():
    print("Hola desde fabfile")

def deploy():
    print(">>> nos conectamos a nuestro servidor remoto.")
    #run('ls')
    #run('whoami')
    
    # Trabajando dentro de un contexto
    with cd('project'):
        with cd('cf_medical'):
            run('ls')
            run('git pull')

            with prefix('source env/bin/activate'): # con prefix activamos el entorno virtual y termina cuando el bloque finaliza
                run('pip install -r requirements.txt')
                # hacer migraciones
                #run('sudo service start mysql')
                run('python manage.py migrate')
                # ejecutar sin que nos pregunte nada, si deseamos sobreescribir
                # simplemente lo va a realizar
                run('python manage.py collectstatic --noinput')

                # ejecutar comandos como sudo
    sudo('service django restart')
    sudo('service nginx restart')

    # reiniciar con systemctl
    #sudo('sudo systemctl restart django')
    #sudo('sudo systemctl restart nginx')
    print('proceso de deploy finalizado')


def master(commit):
    local('git add --all')
    local(f'git commit -m "{commit}"' )
    local('git push origin master')

    







def mkdir(folder):
    command = f'mkdir {folder}'
    run(command)

