# models.py
from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q

class core(models.Model):
    unidades = (
        ('UNIDADES DE ARMAZENAMENTO 1', 'UNIDADES DE ARMAZENAMENTO 1'),
        ('UNIDADES DE ARMAZENAMENTO 2', 'UNIDADES DE ARMAZENAMENTO 2'),
        ('UNIDADES DE GRADEAMENTO 1', 'UNIDADES DE GRADEAMENTO 1'),
        ('UNIDADES DE GRADEAMENTO 2', 'UNIDADES DE GRADEAMENTO 2'),
    )

    STATUS_DO_RASPADOR_DE_GRADEAMENTO = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DA_UNIDADE = (
        ('Ativado', '🟩'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_ENTRADA = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_APARELHO = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    STATUS_DE_SAIDA = (
        ('Ativado', '🟩'),
        ('Manutenção', '🟨'),
        ('Desativado', '🟥'),
    )

    unidades = models.CharField(
        max_length=50,
        choices=unidades,
        verbose_name="Unidades"
    )

    STATUS_DA_UNIDADE = models.CharField(
        max_length=10,
        choices=STATUS_DA_UNIDADE,
        verbose_name="STATUS_DA_UNIDADE",
        default='Ativado'
    )

    STATUS_DE_SAIDA = models.CharField(
        max_length=10,
        choices=STATUS_DE_SAIDA,
        verbose_name="STATUS_DE_SAIDA",
        default='Ativado'
    )

    STATUS_DE_APARELHO = models.CharField(
        max_length=10,
        choices=STATUS_DE_APARELHO,
        verbose_name="STATUS_DE_APARELHO",
        default='Ativado'
    )

    STATUS_DE_ENTRADA = models.CharField(
        max_length=10,
        choices=STATUS_DE_ENTRADA,
        verbose_name="STATUS_DE_ENTRADA",
        default='Ativado'
    )

    STATUS_DO_RASPADOR_DE_GRADEAMENTO = models.CharField(
        max_length=10,
        choices=STATUS_DO_RASPADOR_DE_GRADEAMENTO,
        verbose_name="STATUS_DO_RASPADOR",
        default='Ativado',
    )

    Nivel_de_Potencia_das_Bombas = models.IntegerField(
        verbose_name="Nivel de Potencia das Bombas",
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        # Use Q objects para definir a lógica condicional
        default=None,
        # Condição: Este campo só é visível quando 'UNIDADES DE ARMAZENAMENTO 1' ou 'UNIDADES DE ARMAZENAMENTO 2' for selecionado
        editable=Q(unidades='UNIDADES DE ARMAZENAMENTO 1'),
    )

    Nivel_do_Compartimento_de_gradeamento = models.IntegerField(
        verbose_name="Nivel do Compartimento de Gradeamento",
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        # Use Q objects para definir a lógica condicional
        default=None,
        # Condição: Este campo só é visível quando 'UNIDADES DE GRADEAMENTO 1' for selecionado
        editable=Q(unidades='UNIDADES DE GRADEAMENTO 1'),
    )

    Nivel_do_Tanque = models.IntegerField(
        verbose_name="Nivel do Tanque",
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        # Use Q objects para definir a lógica condicional
        default=None,
        # Condição: Este campo só é visível quando 'UNIDADES DE ARMAZENAMENTO 2' for selecionado
        editable=Q(unidades='UNIDADES DE ARMAZENAMENTO 2'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
