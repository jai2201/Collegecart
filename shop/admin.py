from django.contrib import admin
from .models import Category , item , subcategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(item)
class itemAdmin(admin.ModelAdmin):
	list_display = ['user','category','subcategoryname','title','image','published_on','address','available','price','description']


@admin.register(subcategory)
class subcategoryAdmin(admin.ModelAdmin):
	list_display = ['subcategoryname', 'category']
