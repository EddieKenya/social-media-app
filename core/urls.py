from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login, name='login')
    
]
