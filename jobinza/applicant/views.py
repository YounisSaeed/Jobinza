from django.shortcuts import render , redirect
from company.models import CreatePost
from applicant.models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from company.views import update_status
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from applicant.forms import uploadForm
from applicant.models import contacts
from applicant.forms import contactform
# Create your views here.

@login_required(login_url='login')
def job_details(request , job_id):
    id_num = int(job_id)
    job_list = CreatePost.objects.get(id=id_num)

    return render(request,'applicant/job_details.html', {'job': job_list })

def home(request):   
    update_status()
    listusers = User.objects.all()
    listpost=CreatePost.objects.all()

    return render(request,'applicant/guest.html' , {'posts':listpost , 'users': listusers})

def contact(request):
    if request.method =='POST':
            post=contacts()
            post.fullname=request.POST.get('fullname')
            post.email=request.POST.get('email')
            post.phone=request.POST.get('phone')
            post.message=request.POST.get('message')
            post.save()
            
    
    return render(request,'applicant/contact.html')



@login_required(login_url='login')
def profile_info(request,user_name):
    user_info = User.objects.get(username=user_name)
    pk = User.objects.get(username=user_name).pk
    try:
        profile_info = Profile.objects.get(author = pk)
       # context['title']='profile',
        return render(request,'applicant/profile.html', {'result': user_info , 'info':profile_info } )
    except:
        return render(request,'applicant/profile.html', {'result': user_info , 'info':'' })

def addinfo (request):
    user = request.user
    if request.method == 'POST':
        author = User.objects.filter(username=user.username).first()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ',author)
        job = Profile()
        job.phonenumber = request.POST.get('phone')
        job.address = request.POST.get('address')
        job.author = author
        job.save()
    return render(request, 'applicant/form.html')

@login_required(login_url='login')
def list_applicant(request):
    update_status()
    listusers = User.objects.all()
    listpost=CreatePost.objects.all()

    return render(request,'applicant/home.html', {'posts' : listpost , 'users': listusers} )
