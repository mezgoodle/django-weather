from django.test import TestCase
from .models import City


class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        City.objects.create(name='Kyiv')

    def test_name_content(self):
        task = City.objects.get(id=1)
        expected_object_name = f'{task.name}'
        self.assertEquals(expected_object_name, 'Kyiv')
