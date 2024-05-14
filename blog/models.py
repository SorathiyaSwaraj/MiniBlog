from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    uid                 = models.BigAutoField(primary_key=True)
    username            = models.CharField(max_length=100, unique=True)
    password            = models.CharField(max_length=50)
    email               = models.EmailField(verbose_name="email", max_length=100, unique=True)
    phone_no            = models.CharField(max_length=12, null = True)
    pageviews           = models.BigIntegerField(default = 0)
    total_pages         = models.BigIntegerField(default = 0)
    upi                 = models.CharField(max_length=50, null = True)
    

    def __str__(self):
        return self.username



class Home(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)
	about = models.TextField()
	copyright = models.CharField(max_length=255,blank=True,null=True)
	address = models.CharField(max_length=255,blank=True,null=True)
	phone = models.CharField(max_length=255,blank=True,null=True)
	email = models.CharField(max_length=255,blank=True,null=True)


	def __str__(self):
		return self.title


class Category(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)

	def __str__(self):
		return self.title




class Post(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
	image = models.ImageField(upload_to='images',blank=True,null=True)
	text = RichTextField()
	date = models.DateTimeField(auto_now_add=True)
	slug = AutoSlugField(populate_from='title',null=True)

	def __str__(self):
		return self.title
		

