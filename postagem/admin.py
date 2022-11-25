from django.contrib import admin
from .models import *

class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id','nomeProduto')

# Register your models here.
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Categoria)