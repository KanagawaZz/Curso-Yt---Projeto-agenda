from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Grupo)
admin.site.register(models.Contato)
admin.site.register(models.Telefone)
admin.site.register(models.Email)