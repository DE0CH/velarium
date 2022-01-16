import logging
import re

import google.auth.transport.requests
import google.oauth2.id_token
from django.conf import settings
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

from .logins import get_user
from .models import User
import os
import subprocess


def get_base_context(request):
    """

    :param request: The Django Request object
    :return: A structured dictionary with the context that needs to be
    displayed on all pages, including the User object all all Tag Classes for navigation
    """
    return {
        'user': get_user(request),
        'demo': settings.DEMO,
    }


def index(request):
    """
    This is a Django handler function for the index page
    :param request: The Django Request object
    :return: The index page
    """
    return render(request, 'velarium/index.html', context=get_base_context(request))

def install_keys(request):
    """
    This is a Django handler function for adding a paper into the database. This also handlers form submission through
    HTTP POST.
    :param request: The Django Request object
    :return: Depending on the request method, it either returns the upload UI, or a redirect to the index page
    """
    user = get_user(request)
    context = get_base_context(request)
    if user and not user.registered and request.method == 'POST':
        github_username = request.POST.get('github', '')
        if not validate_github(github_username):
            raise ValueError("Not a valid Github username.")
        if not settings.DEMO:
            print( os.path.join(settings.BASE_DIR, 'make-user.sh'))
            print([os.path.join(settings.BASE_DIR, 'make-user.sh'), f'{user.username}'])
            p = subprocess.run([os.path.join(settings.BASE_DIR, 'make-user.sh'), f'{user.username}'], shell=True)
            print(['sudo',
                                '-u',
                                f'{user.username}',
                                os.path.join(settings.BASE_DIR, 'install-keys.sh'),
                                f'{github_username}'
                                ])
            p = subprocess.run(['sudo',
                                '-u',
                                f'{user.username}',
                                os.path.join(settings.BASE_DIR, 'install-keys.sh'),
                                f'{github_username}'
                                ], shell=True)
            if p.returncode != 0:
                raise ChildProcessError("Failed installing ssh keys")
        user.registered = True
        user.save()
        return redirect('portal:get-user')
    elif user and not user.registered and request.method != 'POST':
        context = get_base_context(request)
        return render(request, 'velarium/get-user.html', context=context)
    elif user and user.registered and request.method == 'POST' and request.POST.get('reset', 'FALSE') == 'TRUE':
        user.registered = False
        user.save()
        return redirect('portal:get-user')
    elif user and user.registered and request.method != 'POST':
        context.update({
            "command_line" : f'ssh {user.username}@{settings.HOST_NAME}',
            "config_file": "Host velarium:\n"
                           f"    HostName {settings.HOST_NAME}\n"
                           f"    User {user.username}",
        })
        return render(request, 'velarium/get-user.html', context=context)
    else:
        return render(request, 'velarium/get-user.html', context=get_base_context(request))


def login(request):
    """
    This is a Django handler function that verifies the login details according to the token gained by signing in with
    Google. Designed to be interacted programmatically
    :param request: The Django Request object
    :return: The login status in JSON format
    """
    if request.method == 'POST':
        id_token = request.POST['id-token']
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            id_info = google.oauth2.id_token.verify_oauth2_token(id_token,
                                                                 google.auth.transport.requests.Request(),
                                                                 settings.G_CLIENT_ID)

            user = User.objects.get_or_create(pk=id_info['sub'])[0]
            user.email = id_info['email']
            user.name = id_info['name']
            user.given_name = id_info['given_name']
            user.family_name = id_info['family_name']
            user.save()
            request.session['sub'] = user.pk
            success = True
        except ValueError:
            # Invalid token
            success = False
    else:
        raise Http404()
    return JsonResponse({
        'success': success
    })

def logout(request):
    """
    This is a Django handler function that logs the current user out. Designed to be accessed programmatically.
    :param request:
    :return:
    """
    try:
        del request.session['sub']
        success = True
    except KeyError:
        success = False
    return JsonResponse({'success': success})


def handler404(request, exception):
    """
    This is a Django handler function designed to override the default 404 page to provide a nicer formatting that is
    consistent with the rest of the website
    :param request: The Django Request object
    :param exception: The Exception caught
    :return: The 404 page
    """
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '404 Not Found',
            'description': 'This is no the web page you are looking for.',
        }
    })
    return render(request, 'velarium/base.html', context=context, status=404)


# noinspection PyBroadException
def handler500(request):
    """
    This is a Django handler function for the 500 server error page. Because a server error can imply an serious issue
    such as corrupted database, a nice render of the 500 page may be impossible. So the server first attemps to nicely
    render the page with all the dynamic element, if it fails, it falls back to the safest render which does not contain
    any dynamic element
    :param request: The Django request object
    :return: The 500 error page
    """
    try:
        context = get_base_context(request)
        context.update({
            'message': {
                'title': '500 Server Error',
                'description': 'Something went wrong. Please try again later.'
            }
        })
        return render(request, 'velarium/base.html', context=context, status=500)
    except:
        return render(request, 'velarium/500.html', status=500)


def handler403(request, exception):
    """
    This is a Django handler function for HTTP 403 permission error
    :param request: The Django Request object
    :param exception: The exception caught
    :return: The 403 error page
    """
    logging.exception(exception)
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '403 Permission Denied',
            'description': 'Looks like you don\'t have the permission to perform the action.'
        }
    })
    return render(request, 'velarium/base.html', context=context, status=403)


def handler400(request, exception):
    """
    This is a Django handler function for 400 Bad Request error
    :param request: The Django Request object
    :param exception: The exception caught
    :return: The 400 error page
    """
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '400 Bad Request',
            'description': 'Your client has issued a malformed or illegal request.'
        }
    })
    return render(request, 'velarium/base.html', context=context, status=400)


def invoke_500(request):
    raise Exception


def demo_login(request):
    if settings.DEMO:
        user = User.objects.get_or_create(pk="demo")[0]
        user.email = "demo@demo.com"
        user.name = "Demo User"
        user.type = 3
        user.save()
        request.session['sub'] = user.pk
        user.registered = False
        return redirect('portal:index')
    else:
        return Http404()

def validate_github(username):
    github_pattern = re.compile('^[a-z\\d](?:[a-z\\d]|-(?=[a-z\\d])){0,38}$')
    return bool(github_pattern.match(username))
