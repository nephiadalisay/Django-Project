from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
	entry_title = models.CharField(max_length=50)
	entry_text = models.TextField()
	entry_date = models.DateTimeField(auto_now_add=True)
	entry_author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True)

	class Meta:
		verbose_name_plural = "entries"
		ordering = ['-entry_date',]


	# if u print the entry, lalabas ung title niya
	def __str__(self):
		return f'{self.entry_title}'

class Comment (models.Model):
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='comments')
	comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	comment_date = models.DateTimeField(auto_now_add=True)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text

