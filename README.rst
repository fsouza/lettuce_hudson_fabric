Continuous integration and deployment with Lettuce, Fabric and Hudson
=====================================================================

A simple Django project wich aims show how to use CI, DI and BDD together.

The toolbox contains:

  #. `Django <http://www.djangoproject.com>`_, a powerful web framework for Python;
  #. `Lettuce <http://lettuce.it>`_, a BDD framework for Python, inspired by Cucumber;
  #. `Fabric <http://fabfile.org>`_, a Python tool for building and deploying applications;
  #. `Hudson <http://hudson-ci.org>`_, a simple, powerful and extensible continuous integration server.

Dependencies
------------

To use this project, you need to install the following tools: Fabric, Django, PyCrypto, Nose, NoseDjango and Lettuce.

You can install all this stuff with only a simple command: ::

  $ [sudo] pip install fabric pycrypto django nose nosedjango lettuce

That will work only if you use PIP. If you don't use PIP (or setuptools), then you will need to install everything manually. So, good luck :)
