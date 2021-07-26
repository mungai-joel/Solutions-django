
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import createuser , ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm



# Create your views here.
def register(request):
    form=createuser()
    if request.user.is_authenticated:
        return redirect('index.html')

    else:
        if request.method=='POST':
            form=createuser(request.POST)
            print(form.errors)
            
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect('/accounts/login')

    context ={'form': form}
    return render(request, 'accounts/register.html',context)





def authlogin(request):
	if request.user.is_authenticated:
		return redirect('index.html')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

@login_required
def index(request):
    context = {}
    return render(request, 'index.html',context)

def Aboutus(request):
    context = {}
    return render(request, 'About-us.html',context)


def access(request):
    context = {}
    return render(request, 'Access.html',context)

def CCTV(request):
    context = {}
    return render(request, 'CCTV.html',context)

@login_required
def contacts(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, '/index')

    form = ContactForm()
    context = {'form': form}

    return render(request, 'contacts.html',context)


def Hardware(request):
    context = {}
    return render(request, 'Haredware & software.html',context)

def networking(request):
    posts = Post.objects.all()


    return render(request, 'Networking.html',{'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('/post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'form': form})

@login_required
def outsourcing(request):
    context = {}
    return render(request, 'Outsourcing.html',context)

@login_required
def support(request):
    context = {}
    return render(request, 'support.html',context)

@login_required
def telecom(request):
    context = {}
    return render(request, 'telecom.html',context)



def authlogout(request):
    logout(request)
    return redirect('/accounts/login')
