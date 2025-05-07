from django.shortcuts import render


# Create your views here.
def home(request):
    """A simple view to return a welcome message."""
    return render(
        request,
        'recipes/home.html',
        context={
            'name': "Kauã Lima"
        }
    )
