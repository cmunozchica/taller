from django.contrib import admin

# Register your models here.
from .models import *

class EquipoAdmin(admin.ModelAdmin):
  list_display = ("serie", "marca", "modelo", "accesorio", "contador", "created", "update",)

admin.site.register(Equipo, EquipoAdmin)