from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(verbose_name="Book Title",max_length=50, null=True)
	author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)


class Author(models.Model):
	name = models.CharField("Auther Name", max_length=50)
