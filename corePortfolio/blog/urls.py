from django.urls import path, include
from blog import views
urlpatterns = [
        path('Blog', views.blogHome, name="Blog"),
        path('addReview', views.add_Review, name="addReview"),
        path('Read_Post/<int:id>', views.readPost, name="Read_Post"),
]