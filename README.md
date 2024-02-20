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