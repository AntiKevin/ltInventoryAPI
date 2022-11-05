from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MaoDeObraSerializer, EquipamentosSerializer
from .models import Equipamentos, MaoDeObra


class EquipamentosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    queryset = Equipamentos.objects.all()
    serializer_class = EquipamentosSerializer
    
class MaoDeObraViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    queryset = MaoDeObra.objects.all()
    serializer_class = MaoDeObraSerializer