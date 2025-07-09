from django.db import models

# Create your models here.
class Palavra(models.Model):
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.texto
    


class Partida(models.Model):
    palavra = models.ForeignKey(Palavra, on_delete=models.CASCADE)
    letras_certas = models.CharField(max_length=100, blank=True)
    letras_erradas = models.CharField(max_length=100, blank=True)
    jogador = models.CharField(max_length=100)
    finalizada = models.BooleanField(default=False)
    venceu = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
