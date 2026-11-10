from django.contrib import admin
from .models import Livros
from .models import Categoria


admin.site.register(Categoria)
admin.site.register(Livros)

