# Tabele-integrate 

# Tabele integrate (Taskmanager5)

1. Create a folder with name taskmanager5
2. Deschide folderul creat in code editor si de acolo deschide terminalul
3. in terminal punem urmatoarele comenzi:
    
    1) django-admin startproject taskmanager5
    
    2) django-admin startapp main5
    
4. in settings → INSTALLED_APPS → main5. Example:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
		'main5',
]
```

1. Dupa in models scriem:

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    slug = models.SlugField(max_length = 255, unique = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        vertoose_name_plural = 'categories'
    def __str__(self):
        return self.name
```

1. Inregistram tabelul in admin:

```python
from django.contrib import admin
from.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name')}
```