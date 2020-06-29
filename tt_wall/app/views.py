from django.shortcuts import render

from tt_wall.app.models import Image


def index(request):
    """View function for the home page."""
    context = {'images': Image.objects.all()}
    return render(request, 'index.html', context=context)
