
from rest_framework import serializers
from .models import Equipamentos, MaoDeObra

class EquipamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamentos
        fields = ['id','nome', 'contrato', 'responsavel']
        
class MaoDeObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaoDeObra
        fields = ['user','cargo', 'contrato', 'vinculo']