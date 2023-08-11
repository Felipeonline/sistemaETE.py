# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), #Path vazio de propósito para o login ser a página inicial
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Página de redirecionamento após o login bem-sucedido
    #path('dashboard/ativos/', views.ativos_view, name='ativos'),
    #path('dashboard/ativos/estatisticasAleatorias/', views.ativosEstatisticas_view, name='ativos'),
    #path('dashboard/estatisticasAleatorias/', views.estatisticasAleatorias_view, name='estatisticasAleatorias'),
    path('dashboard/armazenamento', views.armazenamento_view, name='armazenamento'),
    path('dashboard/armazenamento/historico', views.armazenamentoHistorico_view, name='armazenamentoHistorico'),
    path('dashboard/gradeamento', views.gradeamento_view, name='gradeamento'),
]