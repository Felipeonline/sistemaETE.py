from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q

class HistoricoAtivacao(models.Model):
    ativo = models.CharField(max_length=255)
    acao = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ativo} - {self.acao}"

class ARMAZENAMENTO_1(models.Model):
    ARMAZENAMENTO_1 = (
        ('ARMAZENAMENTO_1', 'UNIDADES DE ARMAZENAMENTO 1'),
    )

    STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_APARELHO_DE_ARMAZENAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_SAIDA_DE_ARMAZENAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    ARMAZENAMENTO_1 = models.CharField(
        max_length=100,
        choices=ARMAZENAMENTO_1,
        verbose_name="ARMAZENAMENTO_1"
    )

    STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_1 = models.CharField(
        max_length=50,
        choices=STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_1,
        verbose_name="STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_1",
        default='Ativado'
    )

    STATUS_DE_SAIDA_DE_ARMAZENAMENTO_1 = models.CharField(
        max_length=50,
        choices=STATUS_DE_SAIDA_DE_ARMAZENAMENTO_1,
        verbose_name="STATUS_DE_SAIDA_DE_ARMAZENAMENTO_1",
        default='Ativado'
    )

    STATUS_DE_APARELHO_DE_ARMAZENAMENTO_1 = models.CharField(
        max_length=50,
        choices=STATUS_DE_APARELHO_DE_ARMAZENAMENTO_1,
        verbose_name="STATUS_DE_APARELHO_DE_ARMAZENAMENTO_1",
        default='Ativado'
    )

    STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_1 = models.CharField(
        max_length=50,
        choices=STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_1,
        verbose_name="STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_1",
        default='Ativado'
    )

    Nivel_de_Potencia_das_Bombas = models.IntegerField(
        verbose_name="Nivel de Potencia das Bombas",
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        # Use Q objects para definir a lógica condicional
        default=None,
        # Condição: Este campo só é visível quando 'UNIDADES DE ARMAZENAMENTO 1' ou 'UNIDADES DE ARMAZENAMENTO 2' for selecionado
        editable=Q(ARMAZENAMENTO_1='ARMAZENAMENTO_1'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ARMAZENAMENTO_2(models.Model):
    ARMAZENAMENTO_2= (
        ('ARMAZENAMENTO_2', 'UNIDADES DE ARMAZENAMENTO 2'),

    )

    STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_APARELHO_DE_ARMAZENAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_SAIDA_DE_ARMAZENAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    ARMAZENAMENTO_2 = models.CharField(
        max_length=50,
        choices=ARMAZENAMENTO_2,
        verbose_name="ARMAZENAMENTO_2"
    )

    STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_2,
        verbose_name="STATUS_DA_UNIDADE_DE_ARMAZENAMENTO_2",
        default='Ativado'
    )

    STATUS_DE_SAIDA_DE_ARMAZENAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DE_SAIDA_DE_ARMAZENAMENTO_2,
        verbose_name="STATUS_DE_SAIDA_DE_ARMAZENAMENTO_2",
        default='Ativado'
    )

    STATUS_DE_APARELHO_DE_ARMAZENAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DE_APARELHO_DE_ARMAZENAMENTO_2,
        verbose_name="STATUS_DE_APARELHO_DE_ARMAZENAMENTO_2",
        default='Ativado'
    )

    STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_2,
        verbose_name="STATUS_DE_ENTRADA_DE_ARMAZENAMENTO_2",
        default='Ativado'
    )

    Nivel_do_Tanque = models.IntegerField(
        verbose_name="Nivel do Tanque",
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        # Use Q objects para definir a lógica condicional
        default=None,
        # Condição: Este campo só é visível quando 'UNIDADES DE ARMAZENAMENTO 2' for selecionado
        editable=Q(ARMAZENAMENTO_2='ARMAZENAMENTO 2'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GRADEAMENTO_1(models.Model):
    GRADEAMENTO_1= (
        ('UNIDADES DE GRADEAMENTO 1', 'UNIDADES DE GRADEAMENTO 1'),
    )

    STATUS_DO_RASPADOR_DE_GRADEAMENTO_DE_GRADEAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DA_UNIDADE_DE_GRADEAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_ENTRADA_DE_GRADEAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_APARELHO_DE_GRADEAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_SAIDA_DE_GRADEAMENTO_1 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    GRADEAMENTO_1 = models.CharField(
        max_length=50,
        choices=GRADEAMENTO_1,
        verbose_name="GRADEAMENTO_1"
    )

    STATUS_DA_UNIDADE_DE_GRADEAMENTO_1= models.CharField(
        max_length=10,
        choices=STATUS_DA_UNIDADE_DE_GRADEAMENTO_1,
        verbose_name="STATUS_DA_UNIDADE_DE_GRADEAMENTO_1",
        default='Ativado'
    )

    STATUS_DE_SAIDA_DE_GRADEAMENTO_1 = models.CharField(
        max_length=10,
        choices=STATUS_DE_SAIDA_DE_GRADEAMENTO_1,
        verbose_name="STATUS_DE_SAIDA",
        default='Ativado'
    )

    STATUS_DE_APARELHO_DE_GRADEAMENTO_1 = models.CharField(
        max_length=10,
        choices=STATUS_DE_APARELHO_DE_GRADEAMENTO_1,
        verbose_name="STATUS_DE_APARELHO_DE_GRADEAMENTO_1",
        default='Ativado'
    )

    STATUS_DE_ENTRADA_DE_GRADEAMENTO_1 = models.CharField(
        max_length=10,
        choices=STATUS_DE_ENTRADA_DE_GRADEAMENTO_1,
        verbose_name="STATUS_DE_ENTRADA_DE_GRADEAMENTO_1",
        default='Ativado'
    )

    STATUS_DO_RASPADOR_DE_GRADEAMENTO_DE_GRADEAMENTO_1 = models.CharField(
        max_length=10,
        choices=STATUS_DO_RASPADOR_DE_GRADEAMENTO_DE_GRADEAMENTO_1,
        verbose_name="STATUS_DO_RASPADOR_DE_GRADEAMENTO_1",
        default='Ativado',
    )

    Nivel_do_Compartimento_de_gradeamento = models.IntegerField(
        verbose_name="Nivel do Compartimento de Gradeamento",
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        # Use Q objects para definir a lógica condicional
        default=None,
        # Condição: Este campo só é visível quando 'UNIDADES DE GRADEAMENTO 1' for selecionado
        editable=Q(GRADEAMENTO_1='UNIDADE DE GRADEAMENTO 1'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GRADEAMENTO_2(models.Model):
    GRADEAMENTO_2 = (
        ('UNIDADES DE GRADEAMENTO 2', 'UNIDADES DE GRADEAMENTO 2'),
    )

    STATUS_DO_RASPADOR_DE_GRADEAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DA_UNIDADE_DE_GRADEAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_ENTRADA_DE_GRADEAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_APARELHO_DE_GRADEAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_SAIDA_DE_GRADEAMENTO_2 = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    GRADEAMENTO_2 = models.CharField(
        max_length=50,
        choices=GRADEAMENTO_2,
        verbose_name="GRADEAMENTO_2"
    )

    STATUS_DA_UNIDADE_DE_GRADEAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DA_UNIDADE_DE_GRADEAMENTO_2,
        verbose_name="STATUS_DA_UNIDADE_DE_GRADEAMENTO_2",
        default='Ativado'
    )

    STATUS_DE_SAIDA_DE_GRADEAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DE_SAIDA_DE_GRADEAMENTO_2,
        verbose_name=" STATUS_DE_SAIDA_DE_GRADEAMENTO_2",
        default='Ativado'
    )

    STATUS_DE_APARELHO_DE_GRADEAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DE_APARELHO_DE_GRADEAMENTO_2,
        verbose_name="STATUS_DE_APARELHO_DE_GRADEAMENTO_2",
        default='Ativado'
    )

    STATUS_DE_ENTRADA_DE_GRADEAMENTO_2 = models.CharField(
        max_length=10,
        choices=STATUS_DE_ENTRADA_DE_GRADEAMENTO_2,
        verbose_name="STATUS_DE_ENTRADA_DE_GRADEAMENTO_2",
        default='Ativado'
    )

    STATUS_DO_RASPADOR_DE_GRADEAMENTO_2= models.CharField(
        max_length=10,
        choices=STATUS_DO_RASPADOR_DE_GRADEAMENTO_2,
        verbose_name="STATUS_DO_RASPADOR_DE_GRADEAMENTO_2",
        default='Ativado',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
