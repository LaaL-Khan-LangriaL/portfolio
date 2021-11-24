from django.urls import path, include
from index import views


urlpatterns = [
    path('Portfolio', views.Home, name="Portfolio"),
    path('sh', views.Home, name="sh"),
    path('sayhello', views.sayhello, name="sayhello"),
]
