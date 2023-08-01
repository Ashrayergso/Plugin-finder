```python
from django.shortcuts import render
from .models import Plugin
from .utils import scan_plugins, get_plugin_data, check_version

def home(request):
    return render(request, 'plugin_scanner/home.html')

def plugin_table(request):
    plugins = Plugin.objects.all()
    return render(request, 'plugin_scanner/plugin_table.html', {'plugins': plugins})

def search_plugin(request):
    if request.method == 'POST':
        plugin_name = request.POST.get('plugin_name')
        plugins = scan_plugins(plugin_name)
        for plugin in plugins:
            Plugin.objects.create(name=plugin.name, version=plugin.version, creator=plugin.creator, installation_date=plugin.installation_date)
        return render(request, 'plugin_scanner/search_plugin.html', {'plugins': plugins})
    else:
        return render(request, 'plugin_scanner/search_plugin.html')

def check_version(request, plugin_id):
    plugin = Plugin.objects.get(id=plugin_id)
    latest_version = check_version(plugin.name)
    return render(request, 'plugin_scanner/check_version.html', {'plugin': plugin, 'latest_version': latest_version})
```