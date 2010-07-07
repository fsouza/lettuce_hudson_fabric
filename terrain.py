# -*- coding: utf-8 -*-
from lettuce import before, after, world
from selenium import get_driver, FIREFOX
from django.conf import settings

@before.all
def setup_browser():
    world.browser = get_driver(FIREFOX)
    settings.DEBUG = True

@after.all
def teardown_browser(total):
    world.browser.quit()

