from .models import User

def get_user(request):
    """
    :param request: the django request object
    :return: a dictionary of the information of the user
    Get a dictionary of the currently logged in user
    """
    try:
        sub = request.session['sub']
        user = User.objects.get(pk=sub)
        return user
    except (KeyError, User.DoesNotExist):
        return None
