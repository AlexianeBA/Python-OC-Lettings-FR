from django.shortcuts import render
from .models import Profile


# Create your views here.
def index(request):
    """
    View function for the index page.

    Retrieves all profiles from the database and renders them on the index.html template.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response containing the index page with the profiles.

    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    print(profiles_list)
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View function to display the profile of a user.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being viewed.

    Returns:
        HttpResponse: The HTTP response object containing the rendered profile template.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profiles": profile}
    return render(request, "profiles/profile.html", context)
