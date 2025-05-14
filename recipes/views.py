from django.shortcuts import render


def home(request):
    """View function for home page of site."""
    return render(request, 'recipes/home.html', context={
        'author': 'kaualima',
    })
# Create your views here.
