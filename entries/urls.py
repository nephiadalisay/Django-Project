from django.urls import path
from .views import HomeView, EntryView, post_entry, delete_entry, add_comment_to_post, delete_comment

urlpatterns = [
	path('', HomeView.as_view(), name="blog-home"), # at least need 2 parametes, root & view
	path('entry/<int:pk>/', EntryView.as_view(), name="entry-detail"),
	path('create_entry/', post_entry, name="create_entry"),
	path('entry/<int:pk>/remove', delete_entry, name="delete-entry"),
	path('entry/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
	path('comment/<int:pkcom>/<int:pkent>/remove', delete_comment, name='delete_comment'),

]