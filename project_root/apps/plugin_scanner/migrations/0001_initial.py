```python
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=50)),
                ('creator', models.CharField(max_length=200)),
                ('installation_date', models.DateTimeField()),
            ],
        ),
    ]
```