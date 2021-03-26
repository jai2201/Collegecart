from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name

class subcategory(models.Model):
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	subcategoryname=models.TextField(null=False,blank=False)

	def __str__(self):
		return str(self.category)+'-'+str(self.subcategoryname)


class item(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	image=models.ImageField(null= False, blank=False, upload_to="itemimage" )
	title=models.TextField(null=False, blank=False)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	published_on=models.DateTimeField(auto_now=True)
	address=models.TextField(null=False, blank=False)
	description=models.CharField(max_length=1000, null=False, blank=False)
	available = models.BooleanField(default=True)
	subcategoryname=models.ForeignKey(subcategory, on_delete=models.CASCADE)


	def __str__(self):
		return self.description
