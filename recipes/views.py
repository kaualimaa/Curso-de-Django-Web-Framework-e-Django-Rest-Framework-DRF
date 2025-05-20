from django.shortcuts import render


def home(request):
    """View function for home page of site."""
    return render(request, 'recipes/pages/home.html')
# Create your views here.
