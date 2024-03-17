from django.shortcuts import render


def index(request):
    """
    Renders the index.html template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered index.html template.
    """
    return render(request, "index.html")


def handler404(request):
    """
    Custom 404 error handler.

    This function handles the 404 error and renders the "404.html" template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered "404.html" template with a status code of 404.
    """
    return render(request, "404.html", status=404)


def handler500(request):
    """
    Custom error handler for HTTP 500 Internal Server Error.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered 500.html template with a status code of 500.
    """
    return render(request, "500.html", status=500)
