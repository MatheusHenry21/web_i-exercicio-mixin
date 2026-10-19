from django.contrib.auth import views as auth_views
from django.urls import path

from .views import PainelView, HomeView, PerfilView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('painel/', PainelView.as_view(), name='painel'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html', next_page='painel'), name='login'),
    path('perfil/', PerfilView.as_view(), name='perfil',),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
