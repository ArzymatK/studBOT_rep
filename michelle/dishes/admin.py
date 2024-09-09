from django.contrib import admin
from .models import Category, SubCategory, SVG, Dish

admin.site.register([Category, SubCategory, SVG, Dish])
