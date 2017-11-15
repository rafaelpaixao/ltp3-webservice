from django.contrib import admin

# Register your models here.
from .models import Aluno, Turma

admin.site.register(Aluno)
admin.site.register(Turma)