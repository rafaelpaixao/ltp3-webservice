from rest_framework import viewsets
from .serializers import *
from .models import *

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    http_method_names = ['get']

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    http_method_names = ['get']