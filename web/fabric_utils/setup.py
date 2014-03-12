from importlib import import_module
from fabric.api import cd, run, sudo
from deploy import deploy


def setup_server():
    packages = [
        'git',
        'python-virtualenv',
        'mercurial',
        'python-psycopg2',
        'postgresql',
        'python-flup',
        'nginx'
    ]

    for package in packages:
        sudo('apt-get install --yes {0}'.format(package))

    username = run('echo $USER')

    sudo('addgroup webadmin')
    sudo('adduser {0} webadmin'.format(username))

    sudo('mkdir /var/www')
    sudo('mkdir /var/www/python')
    sudo('chgrp -R webadmin /var/www')
    sudo('chmod -R ug+w /var/www')

    sudo('createuser -E -P -s {0}'.format(username), user='postgres')
    run('createuser -s root')

    sudo('mkdir /var/fastcgi')
    sudo('chmod 777 /var/fastcgi')
    sudo('rm /etc/nginx/sites-enabled/default')
    sudo('/etc/init.d/nginx start')


def setup_deployment(config, repo):
    settings = import_module('guidcoin.settings_{0}'.format(config))
    PYTHON_DIR = '/var/www/python'
    repo_dir = '{0}/guidcoin-{1}'.format(PYTHON_DIR, config)

    with cd(PYTHON_DIR):
        run('git clone {0} guidcoin-{1}'.format(repo, config))

    with cd(repo_dir):
        run('virtualenv --system-site-packages venv')

    deploy(config)
