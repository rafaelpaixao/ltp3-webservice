from django.db import models
import datetime


SEMESTER_CHOICES = ((1, 'Primeiro'),(2, 'Segundo'))
YEAR_CHOICES = [(r,r) for r in range(2010, datetime.date.today().year+4)]


class Turma(models.Model):

    disciplina = models.CharField(max_length=100, verbose_name=u"Disciplina")
    alunos = models.ManyToManyField('Aluno', blank=True, verbose_name=u"Alunos")

    semestre = models.IntegerField(choices=SEMESTER_CHOICES,default=1, verbose_name=u"Semestre")
    ano = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, verbose_name=u"Ano")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ano)+"."+str(self.semestre)+"."+str(self.id)+"-"+self.disciplina


class Aluno(models.Model):

    nome = models.CharField(max_length=100, verbose_name=u"Nome")
    turmas = models.ManyToManyField('Turma', through=Turma.alunos.through, blank=True, verbose_name=u"Turmas")

    semestre = models.IntegerField(choices=SEMESTER_CHOICES,default=1, verbose_name=u"Semestre")
    ano = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, verbose_name=u"Ano")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.nome