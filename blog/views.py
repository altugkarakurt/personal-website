from django.shortcuts import render

def home(request):
    return render(request, "blog/home.html", {'title':'Home'})


def about(request):
    return render(request, "blog/about.html", {'title':'About'})


def blog(request):
    return render(request, "blog/index.html", {'title':'Blog'})


def projects(request):
    return render(request, "blog/projects.html", {'title':'Projects'})