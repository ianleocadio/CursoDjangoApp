from django.urls import path

from . import views


app_name = "accounts"
urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('alterar-senha/', views.change_password, name='change_password'),
]