from django.contrib import admin

from .models import NewsStory

admin.site.register(NewsStory)


from .models import Category

admin.site.register(Category)