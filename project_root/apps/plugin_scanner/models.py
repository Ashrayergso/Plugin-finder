```python
from django.db import models

class Plugin(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=50)
    creator = models.CharField(max_length=200)
    installation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```