from django.contrib import admin

from  .models import Category, Question

myModels = [ Category, Question]
admin.site.register(myModels)

# Register your models here.
