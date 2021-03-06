from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .models import Project, Blog, Skill, Connection,Experience,Profile
# Create your views here.
from .forms import NameForm
from django.core.mail import send_mail


def index(request):
   
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:5]
    profile = Profile.objects.all().first()
    form = NameForm()
    context = {'projects': projects, 'skills': skills, 'form': form,'experiences':experiences,'profile':profile}
    return render(request, 'index.html', context)


def experiences(request):
    return HttpResponse("you are in experience page")


def blogs(request):
    
    blogs = Blog.objects.all().order_by('-published_on')
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)


def contact(request):
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ob = Connection()
            ob.your_name = form.cleaned_data['your_name']
            ob.email = form.cleaned_data['email']
            ob.subject = form.cleaned_data['subject']
            ob.message = form.cleaned_data['message']
            ob.save()
            context={}
            return render(request, 'contact.html', context)
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'contact.html')


def projects(request):
    return HttpResponse("you are in projects pages")