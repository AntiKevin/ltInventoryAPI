from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Equipamentos(models.Model):
    nome = models.CharField(max_length=255)
    contrato = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True, editable=False, blank=False)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.none
    
class MaoDeObra(models.Model):
    cargo = models.CharField(max_length=255)
    contrato = models.CharField(max_length=255)
    vinculo = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.none