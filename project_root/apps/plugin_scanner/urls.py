```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scan/', views.scan_plugins, name='scan_plugins'),
    path('plugins/', views.plugin_table, name='plugin_table'),
    path('search/', views.search_plugin, name='search_plugin'),
    path('check_version/', views.check_version, name='check_version'),
]
```