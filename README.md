# Tabele-integrate 

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
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
```

1. Inregistram tabelul in admin:

```python
from django.contrib import admin
from . models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
```

1. Dupa facem migratiile si creeam superuserul.
2. Continuam cu [models.py](http://models.py) 

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    slug = models.SlugField(max_length = 255, unique = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE)
    create_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'product_creator')
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255, default = 'admin')
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length = 255, unique = True)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    in_stock = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
```