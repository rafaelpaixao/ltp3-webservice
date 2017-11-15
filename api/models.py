from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, verbose_name=u"Nome")
    semestre = models.IntegerField(default=1, verbose_name=u"Semestre de Ingresso")
    ano = models.IntegerField(verbose_name=u"Ano de Ingresso")

    def __str__(self):
        return self.nome

class Turma(models.Model):
    disciplina = models.CharField(max_length=100, verbose_name=u"Disciplina")
    semestre = models.IntegerField(default=1, verbose_name=u"Semestre de Ingresso")
    ano = models.IntegerField(default=2017, verbose_name=u"Ano de Ingresso")

    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.disciplina