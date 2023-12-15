from django.db import models
from django.test import TestCase
from flowersite.models import models

class Receipt(models.Model):
    shopname = models.CharField(max_length=100, default="Default Shop")
    description = models.TextField(default="description", blank=True)
    total = models.TextField(default="total", blank=True)

    def __str__(self):
        return self.shopname

class YourModelTest(TestCase):
    def test_create_instance(self):
        obj = models.objects.create(name="Test")
        self.assertEqual(obj.name, "Test")

    