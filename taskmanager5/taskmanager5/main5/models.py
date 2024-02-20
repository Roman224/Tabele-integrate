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