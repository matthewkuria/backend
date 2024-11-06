from django.contrib import admin
from news.models import NewsCategory, News
# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(News)
