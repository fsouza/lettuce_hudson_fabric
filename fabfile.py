from fabric.api import local

def test():
    """This function calls nosetests"""
    local('nosetests --with-django', capture=False)

def spec():
    """This function runs harvest"""
    local('python manage.py harvest', capture=False)

def pack():
    """This function packs the project"""
    local('tar czf /tmp/project_to_deploy.tar.gz .', capture=False)

def prepare_deploy():
    test()
    spec()
    pack()
