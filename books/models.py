from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):
	title = models.CharField(verbose_name="Book Title",max_length=50, null=True)
	author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True,blank=True)

	def __str__(self):
		return "%s"%(self.title)
		
	def get_absolute_url(self):
		return reverse("books:book_detail",kwargs={"book_id":self.id})


class Author(models.Model):
	name = models.CharField("Auther Name", max_length=50)
