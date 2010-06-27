# -*- coding: utf-8 -*-
from lettuce import *
from lettuce.django import django_url

from django.contrib.auth.models import User

from school.models import Student

@before.each_scenario
def clear_users(scenario):
    world.users = []

@before.each_scenario
def clear_students(scenario):
    Student.objects.all().delete()

def usernamefy(name):
    return slugify(name).replace('-', '_')

@step(u'Given there is an user "(.*)" with the password "(.*)"')
def given_there_is_an_user_group1_with_the_password_group2(step, username, password):
    name = username
    email = '%(username)s@%(username)s.com' % locals()
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_superuser(username, email, password)

    user.is_staff = True
    user.is_active = True
    user.is_superuser = True
    user.set_password(password)
    user.save()

    data = type('UserData', (), locals())
    world.users.append(data)
