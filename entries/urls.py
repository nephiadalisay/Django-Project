from django.urls import path
from .views import HomeView, EntryView, CreateEntryView, delete_entry

urlpatterns = [
	path('', HomeView.as_view(), name="blog-home"), # at least need 2 parametes, root & view
	path('entry/<int:pk>/', EntryView.as_view(), name="entry-detail"),
	path('create_entry/', CreateEntryView.as_view(success_url='/'), name="create_entry"),
	path('entry/<int:pk>/remove', delete_entry, name="delete-entry"),

]