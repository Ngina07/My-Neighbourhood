from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class hoodTestClass(TestCase):
    def setUp(self):
        self.Kileleshwa = Hood(hood='Kileleshwa')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kileleshwa,hood))

    

    def test_save_method(self):
        self.Kileleshwa.save_hood()
        hood = hood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Kileleshwa.delete_hood('Kileleshwa')
        hood = hood.objects.all()
        self.assertTrue(len(hood)==0)
    def tearDown(self):
        Hood.objects.all().delete()
class healthTestClass(TestCase):
    def setUp(self):
        self.Hospital = Health(healthservices='Hospital')

    def test_instance(self):
        self.assertTrue(isinstance(self.Hospital,healthservices))

    
    def test_save_method(self):
        self.Hospital.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Hospital.delete_healthservices('Hospital')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)

    def tearDown(self):
        Health.objects.all().delete()
