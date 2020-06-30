from django.shortcuts import redirect, render

from tt_wall.app.models import Image


def index(request):
    """View function for the home page."""
    context = {'images': Image.objects.all()}
    return render(request, 'index.html', context=context)


def category_search(request):
    if 'category' in request.GET and request.GET['category']:
        category_name = request.GET.get('category')

        context = {'images': Image.search_by_category(category_name)}
        return render(request, 'index.html', context)
    return redirect(index)


def location_filter(request, location_name):
    context = {'images': Image.filter_by_location(location_name)}
    return render(request, 'index.html', context)
