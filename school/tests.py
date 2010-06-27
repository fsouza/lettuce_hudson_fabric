"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.db import IntegrityError
from models import Student
from nose.tools import *

class TestStudentAttributesValidations(TestCase):

    def test_name_cannot_be_none(self):
        student = Student(name = None)
        assert_raises(IntegrityError, student.save)
