from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Renders the index page with a list of all lettings.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the lettings list.

    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View function for displaying a single letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to be displayed.

    Returns:
        HttpResponse: The HTTP response object containing the rendered letting template.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
