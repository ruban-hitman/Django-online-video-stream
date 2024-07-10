from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from . models import mysigninform,Registermovie
from . forms import signinform,movieRegisterForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def signinpage(request):
    if request.method == 'POST':
        data = signinform(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'registered')
            return redirect('loginpage')
        else:
            messages.error(request, data.errors)
            return redirect('signinpage')
    else:
        form = signinform()    
        return render(request,'Signin.html', {'forms' : form})

    
def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        psw = request.POST['psw']
        
        try:
            user = mysigninform.objects.get(email = email, password = psw)
        except mysigninform.DoesNotExist:
            messages.error(request, 'user not found')
            return redirect('loginpage')
        else:
            request.session['user_id'] = user.id
            request.session['user_Username'] = user.Username
            messages.success(request,'logged in!')
            return redirect('movie')
    else:
        return render(request, 'login.html')    
    
def moviepage(request):
     data = Registermovie.objects.all()
     return render(request, 'movies.html', {'movies' : data})

def logout(request):
    request.session.flush()
    messages.success(request, 'You have been logged out')
    return redirect('index')

def video_list(request):
    videos = Registermovie.objects.all()
    return render(request, 'Video_list.html', {'videos': videos})

def play_video(request, video_id):
    video = get_object_or_404(Registermovie, id=video_id)
    return render(request, 'play_video.html', {'video': video})

