
from django.shortcuts import (get_object_or_404, render)
from django.views.decorators.http import \
    require_http_methods
from django.views.generic import View
from .models import Category, Question


class ShowCategories(View):
	def get(self, request):
		return render(
			request,
			'organizer/show_categories.html',
			{'categories' : Category.objects.all()}) ## categories represents all Category objects.

def category_detail(request,slug):
	category=get_object_or_404(
		Category,
		slug__iexact=slug)
	return render(
			request,
			'organizer/show_category_detail.html',
			{'category': category })

		

	
