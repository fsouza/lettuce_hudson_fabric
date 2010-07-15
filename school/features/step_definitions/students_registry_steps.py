# -*- coding: utf-8 -*-
from lettuce import *
from lettuce.django import django_url
from django.contrib.auth.models import User
from school.models import Student
from lxml import html
from should_dsl import should

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
    dom = html.fromstring(world.browser.get_page_source())

    needs_login = bool(dom.cssselect('body.login,form#login-form,#id_username,#id_password'))
    if needs_login:
        username = world.browser.find_element_by_id("id_usernam2e")
        password = world.browser.find_element_by_id("id_password")
        submit = world.browser.find_element_by_xpath("//input[@value='Log in']")

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
    world.browser.get(django_url('school/students/new'))

@step(u'And fill the name field with "(.*)"')
def and_fill_the_name_field_with_group1(step, name):
    textfield = world.browser.find_element_by_id('id_name')
    textfield.send_keys(name)

@step(u'And save this student with the code "(.*)"')
def and_save_this_student_with_the_code_group1(step, student_code):
    submit_button = world.browser.find_element_by_id('id_submit')
    submit_button.click()

@step(u'Then I should be redirect to the page of student "(.*)"')
def then_i_should_be_redirect_to_the_page_of_student_group1(step, student_code):
    student_code = int(student_code)
    expected_url = django_url('/school/students/view/%d' %student_code)
    world.browser.get_current_url() |should| equal_to(expected_url)

@step(u'And the page title should contains "(.*)"')
def and_the_page_title_should_contains_group1(step, student_name):
    world.browser.get_title() |should| include(student_name)
