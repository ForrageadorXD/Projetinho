from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nomeProduto = models.CharField(max_length=140)
    descricao = models.TextField()
    valor_produto = models.DecimalField(max_digits=8,decimal_places=2)
    categoria = models.ManyToManyField(Categoria)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, max_length=250)

    def __str__(self):
        return self.nome

