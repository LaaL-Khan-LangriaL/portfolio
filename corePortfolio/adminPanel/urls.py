from django.urls import path, include
from adminPanel import views
urlpatterns = [
        path('', views.adminHome, name="admin"),
        path('admin', views.adminHome, name="admin"),
        path('about', views.adminAbout, name="about"),
        path('experience', views.adminExperience, name="experience"),
        path('education', views.adminEducation, name="education"),
        path('languageskills', views.SkillsLang, name="languageskills"),
        path('portfolios', views.portfolios, name="portfolios"),
        path('recommendation', views.recommendation, name="recommendation"),
        path('user_blog', views.user_blog, name="user_blog"),
        path('socialmedia', views.social_media, name="social_media"),
        path('user_login', views.user_login, name="user_login"),
        path('user_logout', views.user_logout, name="user_logout"),
        path('Register', views.UserRegister, name="Register"),
        path('Delete/<int:id>/<str:type>', views.Delete, name="Delete"),
        path('Update/<int:id>/<str:type>', views.Update, name="Update"),
]
