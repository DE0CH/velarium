def get_user(request):
    """
    :param request: the django request object
    :return: a dictionary of the information of the user
    Get a dictionary of the currently logged in user
    """

    return {
        'can_edit': True,
        'type': 'teacher',
        'first_name': 'John',
        'last_name': 'Smith',
        'email': 'john.smith@example.com',
    }