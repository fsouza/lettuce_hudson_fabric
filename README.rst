Continuous integration and deployment with Lettuce, Fabric and Hudson
=====================================================================

A simple Django project wich aims show how to use CI, DI and BDD together.

The toolbox contains:

  #. `Django <http://www.djangoproject.com>`_, a powerful web framework for Python;
  #. `Lettuce <http://lettuce.it>`_, a BDD framework for Python, inspired by Cucumber;
  #. `Fabric <http://fabfile.org>`_, a Python tool for building and deploying applications;
  #. `Hudson <http://hudson-ci.org>`_, a simple, powerful and extensible continuous integration server;
  #. `Selenium <http://seleniumhq.org>`_, an amazing tool for tests.

Dependencies
------------

To use this project, you need to install the following tools: Fabric, Django, PyCrypto, Nose, NoseDjango, should-dsl, Selenium, lxml and Lettuce.

You can install some of this stuffs with just a simple command: ::

  $ [sudo] pip install fabric pycrypto django nose nosedjango lettuce should-dsl lxml

That will work only if you use PIP. If you don't use PIP (or setuptools), then you will need to install everything manually. So, good luck :)

Selenium
--------

I used Selenium with WebDriver, so you need to checkout the Selenium source and build it manually, with the following commands: ::

  $ svn checkout http://selenium.googlecode.com/svn/trunk/ selenium
  $ cd selenium
  $ [sudo] python setup.py install

And it works fine :)
