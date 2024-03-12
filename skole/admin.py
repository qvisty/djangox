from django.contrib import admin
from .models import Afdeling, Elev, Klasse, Medarbejder, SfoGruppe, SfoModul, Team

# Register your models here.
admin.site.register(Afdeling)
admin.site.register(Elev)
admin.site.register(Klasse)
admin.site.register(Medarbejder)
admin.site.register(SfoGruppe)
admin.site.register(SfoModul)
admin.site.register(Team)
