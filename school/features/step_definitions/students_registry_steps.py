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

def do_login():
    world.browser.get(django_url('/admin/login/'))
    dom = world.browser.get_dom()

    needs_login = bool(dom.cssselect('body.login,form#login-form,#id_username,#id_password'))
    if needs_login:
        username = world.browser.find_element_by_selector("#id_username")
        password = world.browser.find_element_by_selector("#id_password")
        submit = world.browser.find_element_by_selector("input[value='Log in']")

        first_user = world.users[0]
        username.send_keys(first_user.username)
        password.send_keys(first_user.password)
        submit.click()

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

@step(u'When I navigate to the new student page')
def when_i_navigate_to_the_new_student_page(step):
    do_login()
    world.browser.get('/school/students/new')
