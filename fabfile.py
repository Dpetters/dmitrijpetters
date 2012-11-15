from fabric.api import env, sudo, cd, run

STAGING_PASSWORD = "Bulle1tN3at"

__all__= ["restart", "update"]

env.password = STAGING_PASSWORD
env.directory = '/var/www/dmitrijpetters.com'
env.hosts = ['root@staging.umeqo.com']

def update():
    with cd(env.directory):
        run("git pull")
