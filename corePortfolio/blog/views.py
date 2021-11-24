from django.shortcuts import render, HttpResponse, redirect
from adminPanel.models import userBlog
from blog.models import add_Review

# Create your views here.


def blogHome(request):
    allBlog = userBlog.objects.all()
    return render(request, 'blog_home.html', {'allBlog': allBlog})


def readPost(request, id):
    rdPost = userBlog.objects.filter(id=id)
    cmnt = add_Review.objects.filter(id=id)
    return render(request, 'read_post.html', {'rdPost': rdPost, 'cmnt': cmnt})


def add_Review(request):
    if request == 'POST':
        author = request.POST('author')
        email = request.POST('email')
        comment = request.POST('comment')
        sv = add_Review(author=author, email=email, comment=comment)
        sv.save()
        return redirect('/Read_Post')
    else:
        HttpResponse("Something went wrong")