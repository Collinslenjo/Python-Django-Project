from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

#About Page view
class AboutPageView(TemplateView):
	"""docstring for AboutPageView"""
	template_name = "about.html"
		