# -*- coding: utf-8 -*-
from lettuce import before, after, world
from selenium.firefox.webdriver import WebDriver
from django.conf import settings

@before.all
def setup_browser():
    world.browser = WebDriver()
    settings.DEBUG = True

@before.each_step
def update_dom(step):
    world.dom = world.browser.get_dom_when_ready()

@after.all
def teardown_browser(total):
    world.browser.quit()

