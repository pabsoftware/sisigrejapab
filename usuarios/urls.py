from django.urls import path, include
from .views import login_user, logout_user, cad_user, lista_user

urlpatterns = [
    
    path('accounts/login/', login_user, name='login'),
    path('accounts/logout/', logout_user, name='logout'),
    path('accounts/signup/', cad_user, name='signup'),
    path('list_user/', lista_user, name='list_user'),

]