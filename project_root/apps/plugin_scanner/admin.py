```python
from django.contrib import admin
from .models import Plugin

class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'creator', 'installation_date')

admin.site.register(Plugin, PluginAdmin)
```