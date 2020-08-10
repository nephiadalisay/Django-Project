from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry, Comment
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# Create your views here.

class HomeView( ListView): #if u want login required to view this view: LoginRequiredMixin
	model = Entry
	template_name = 'entries/index.html'
	context_object_name = "blog_entries"
	ordering = ['-entry_date']
	paginate_by = 10

class EntryView( DetailView): #if u want login required to view this view: LoginRequiredMixin
	model = Entry
	template_name = 'entries/entry_detail.html'

class CreateEntryView( ModelForm): #if u want login required to view this view: LoginRequiredMixin

	class Meta:
		model = Entry
		fields = ['entry_title', 'entry_text', 'image']

def post_entry(request):
	if request.method == "POST":
		if request.FILES:
			form = CreateEntryView(request.POST, request.FILES)
			if form.is_valid():
				entry = form.save(commit=False)
				entry.entry_author = request.user
				entry.save()
				return redirect('blog-home')
		else:
			form = CreateEntryView(request.POST)
			if form.is_valid():
				entry = form.save(commit=False)
				entry.entry_author = request.user
				entry.save()
				return redirect('blog-home')
	else:
		form = CreateEntryView()
	return render(request, 'entries/create_entry.html', {'form':form})


def delete_entry(request, pk):
	entry = get_object_or_404(Entry, pk=pk)
	entry.delete()
	return redirect('blog-home')

def delete_comment(request, pkcom, pkent):
	comment = get_object_or_404(Comment, pk=pkcom)
	comment.delete()
	entri = 'entry/%s' % pkent
	return redirect('entry-detail', pk=pkent)

class CommentForm(ModelForm):

	class Meta:
		model = Comment
		fields = ['text']

def add_comment_to_post(request, pk):
	entry = get_object_or_404(Entry, pk=pk)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.entry = entry
			comment.comment_author = request.user
			comment.save()
			return redirect('entry-detail', pk=entry.pk)
	else:
		form = CommentForm()
	return render(request, 'entries/add_comment_to_post.html', {'form':form, 'entry':entry})
