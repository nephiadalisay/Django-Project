from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import get_object_or_404, redirect
from entries.models import Entry, Comment

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save() #create the user & save to database
			username = request.POST['username']
			password = request.POST['password1']
			user = authenticate(request,username=username,password=password)
			login(request,user)
			return redirect('blog-home')
	else:
		form = RegistrationForm()

	context = {'form':form}
	return render(request, 'users/register.html', context)

def view_profile(request, pk):
	entry_user = get_object_or_404(User, pk=pk)
	entry_user_posts = Entry.objects.filter(entry_author=entry_user)
	entry_user_comments = Comment.objects.filter(comment_author=entry_user)
	ordering = ['-entry_date']
	return render(request, 'users/profile.html', {'entry_user':entry_user,'entry_user_posts':entry_user_posts,'entry_user_comments':entry_user_comments})	

 
