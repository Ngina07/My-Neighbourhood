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
        self.Radiotherapy = Health(healthservices='Radiotherapy')

    def test_instance(self):
        self.assertTrue(isinstance(self.Radiotherapy,healthservices))

    
    def test_save_method(self):
        self.Radiotherapy.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Radiotherapy.delete_healthservices('Radiotherapy')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)
        
    def tearDown(self):
        Health.objects.all().delete()
