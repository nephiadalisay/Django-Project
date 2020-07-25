from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin, ListView):
	model = Entry
	template_name = 'entries/index.html'
	context_object_name = "blog_entries"
	ordering = ['-entry_date']
	paginate_by = 3

class EntryView(LoginRequiredMixin, DetailView):
	model = Entry
	template_name = 'entries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin, CreateView):
	model = Entry
	template_name = 'entries/create_entry.html'
	fields = ['entry_title', 'entry_text']

	# setting the login user as author of post
	# this method is called when valid form data has been POSTed.
	# It should return an HttpResponse.
	def form_valid(self, form):
		form.instance.entry_author = self.request.user
		return super().form_valid(form)

def delete_entry(request, pk):
	entry = get_object_or_404(Entry, pk=pk)
	entry.delete()
	return redirect('blog-home')
