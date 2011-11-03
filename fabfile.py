from fabric.api import env, sudo, cd, run

STAGING_PASSWORD = "Ang3lInvest1ng"

__all__= ["restart", "update"]

env.password = STAGING_PASSWORD
env.directory = '/var/www/dmitrijpetters.com'
env.hosts = ['root@staging.umeqo.com']

def restart():
    run('service apache2 restart')

def update():
    with cd(env.directory):
        run("git pull")
        restart()