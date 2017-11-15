from rest_framework import serializers
from .models import *

class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'