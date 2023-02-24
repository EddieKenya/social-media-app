from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout '),
    path('settings/', views.settings, name='settings'),
    path('post/', views.post, name='post'),
    path('like/',views.like, name='like'),
    path('comments/', views.comments, name='comments'),
    
]
