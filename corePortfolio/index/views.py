from django.shortcuts import render, HttpResponse, redirect
from adminPanel.models import About, Experience, Education, LangSkill, Portfolios, Recommendations, SocialMedia, \
    userBlog
from index.models import hello
# Create your views here.


def Home(request):
    about = About.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    languages_skills = LangSkill.objects.all()
    Recommendation = Recommendations.objects.all()
    portfolio = Portfolios.objects.all()
    social_media = SocialMedia.objects.all()
    blog = userBlog.objects.all()[:2]
    data = {'about': about, 'experience': experience, 'education': education, 'lang_skill': languages_skills,
            'portfolio': portfolio, 'Recommendation': Recommendation, 'social_media': social_media, 'blog': blog}
    return render(request, 'Home.html', data)


def sayhello(request):
    if request.method == 'POST':
        yourName = request.POST.get('yourName')
        yourSubject = request.POST.get('yourSubject')
        description = request.POST.get('description')
        reg = hello(yourName=yourName, yourSubject=yourSubject, description=description)
        reg.save()
        return render(request, 'Home.html')
