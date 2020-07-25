from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
	entry_title = models.CharField(max_length=50)
	entry_text = models.TextField()
	entry_date = models.DateTimeField(auto_now_add=True)
	entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
			verbose_name_plural = "entries"

	# if u print the entry, lalabas ung title niya
	def __str__(self):
		return f'{self.entry_title}'