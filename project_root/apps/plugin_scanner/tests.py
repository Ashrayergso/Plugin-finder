```python
from django.test import TestCase
from .models import Plugin

class PluginModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Plugin.objects.create(name='Test Plugin', version='1.0', creator='Test Creator', installation_date='2022-01-01')

    def test_name_content(self):
        plugin = Plugin.objects.get(id=1)
        expected_object_name = f'{plugin.name}'
        self.assertEquals(expected_object_name, 'Test Plugin')

    def test_version_content(self):
        plugin = Plugin.objects.get(id=1)
        expected_object_version = f'{plugin.version}'
        self.assertEquals(expected_object_version, '1.0')

    def test_creator_content(self):
        plugin = Plugin.objects.get(id=1)
        expected_object_creator = f'{plugin.creator}'
        self.assertEquals(expected_object_creator, 'Test Creator')

    def test_installation_date_content(self):
        plugin = Plugin.objects.get(id=1)
        expected_object_date = f'{plugin.installation_date}'
        self.assertEquals(expected_object_date, '2022-01-01')
```