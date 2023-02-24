from django.urls import path
from.import views

urlpatterns = [
    path('post/',views.PostAPI.as_view(), name='post-api'),
]