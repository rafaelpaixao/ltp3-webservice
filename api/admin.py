from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Aluno, Turma


class AlunoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Aluno._meta.fields]
    list_display_links = ['nome']


class TurmaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Turma._meta.fields]
    list_display_links = ['disciplina']


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)