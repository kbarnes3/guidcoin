from importlib import import_module
from fabric.api import cd, run, sudo
from deploy import deploy


def setup_server(setup_wins=''):
    base_packages = [
        'git',
        'python-virtualenv',
        'python-psycopg2',
        'postgresql',
        'nginx',
        'uwsgi',
        'uwsgi-plugin-python',
    ]

    _install_packages(base_packages)
    if setup_wins:
        _setup_wins()

    username = run('echo $USER')

    sudo('addgroup webadmin')
    sudo('adduser {0} webadmin'.format(username))

    sudo('mkdir /etc/nginx/ssl')
    sudo('mkdir /var/www')
    sudo('mkdir /var/www/python')
    sudo('chgrp -R webadmin /var/www')
    sudo('chmod -R ug+w /var/www')

    sudo('createuser -E -P -s {0}'.format(username), user='postgres')
    run('createuser -s root')

    sudo('mkdir /var/uwsgi')
    sudo('chmod 777 /var/uwsgi')
    sudo('rm /etc/nginx/sites-enabled/default')
    sudo('/etc/init.d/nginx start')


def _install_packages(packages):
    for package in packages:
        sudo('apt-get install --yes {0}'.format(package))


def _setup_wins():
    wins_packages = [
        'samba',
        'winbind',
    ]

    _install_packages(wins_packages)
    sudo('sed -i s/\'hosts:.*/hosts:          files dns wins/\' /etc/nsswitch.conf')


def setup_deployment(config, repo):
    PYTHON_DIR = '/var/www/python'
    repo_dir = '{0}/guidcoin-{1}'.format(PYTHON_DIR, config)

    with cd(PYTHON_DIR):
        run('git clone {0} guidcoin-{1}'.format(repo, config))

    with cd(repo_dir):
        run('virtualenv --system-site-packages venv')

    deploy(config)
