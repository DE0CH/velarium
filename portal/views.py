from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
import logging
from .logins import get_user
from .models import TagClass, Tag, Paper, User, UserType
import os
from html import unescape
from .pdf_processor import pdf_to_png_and_save, get_text
from threading import Thread
import json
import uuid
from django.conf import settings
from utils import s3_client
import google.oauth2.id_token
import google.auth.transport.requests
from .search_engine import search as s_search
import enum
from django.db import DataError


def get_base_context(request):
    """

    :param request: The Django Request object
    :return: A structured dictionary with the context that needs to be
    displayed on all pages, including the User object all all Tag Classes for navigation
    """
    return {
        'user': get_user(request),
        'tag_classes': TagClass.objects.all()
    }


def index(request):
    """
    This is a Django handler function for the index page
    :param request: The Django Request object
    :return: The index page
    """
    if settings.DEMO:
        user = User.objects.get_or_create(pk="demo")[0]
        user.email = "demo@demo.com"
        user.name = "Demo User"
        user.type = 3
        user.save()
        request.session['sub'] = user.pk
    if request.method == 'POST':
        return redirect('portal:index')
    else:
        context = get_base_context(request)
        return render(request, 'velarium/index.html', context=context)


def search(request):
    """
    This is a Django handler function for the search page. Client would pass information into this function through
    HTTP GET parameters
    :param request: The Django Request object
    :return: The results g
    """
    tags = []
    for tag_class in TagClass.objects.all():
        tag_names = request.GET.getlist(tag_class.name)
        for tag_name in tag_names:
            tag = tag_class.tag_set.get(name=tag_name)
            tags.append(tag)
    terms = request.GET.get('terms', '')
    user = get_user(request)
    papers = s_search(terms, tags, user)
    context = get_base_context(request)
    context.update({
        'page_title': f'{terms}',
        'papers': papers,
    })
    return render(request, 'velarium/results.html', context=context)


def browse(request, tag_class=None, tag=None):
    """
    This is a Django handler function for browsing all papers tagged with a specific tag
    :param request: The Django Request object
    :param tag_class: The name of the Tag Class
    :param tag: The name of the Tag
    :return: The results g
    """

    # Thought about using the pk of the tag, but used name instead as it is more human readable
    tag_class = unescape(tag_class)
    tag = unescape(tag)

    context = get_base_context(request)
    context.update({
        'page_title': tag,
        'papers': Tag.objects.get(name=tag, tag_class__name=tag_class).paper_set.all(),
    })
    return render(request, 'velarium/results.html', context=context)


def all_papers(request):
    """
    This is a Django handler function for browser all papers in the database
    :param request: The Django Request object
    :return: The results page
    """
    context = get_base_context(request)
    context.update({
        'page_title': 'All Papers',
        'papers': Paper.objects.all(),
        'all_papers': True
    })
    return render(request, 'velarium/results.html', context=context)


class UploadOption(enum.IntEnum):
    """
    This Enum specifies all upload options and their associated integer value that is used in the front end as well
    """
    FILE = 1
    LINK = 2


def add_paper(request):
    """
    This is a Django handler function for adding a paper into the database. This also handlers form submission through
    HTTP POST.
    :param request: The Django Request object
    :return: Depending on the request method, it either returns the upload UI, or a redirect to the index page
    """
    if get_user(request) and get_user(request).can_edit:
        if request.method == 'POST':
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            paper = Paper(title=title, description=description)
            # Did not supply default value because it's better to crash and notify user and dev than silently fail.
            upload_option = UploadOption(int(request.POST['upload-option']))
            if upload_option == UploadOption.FILE:
                pdf_key = request.POST.get('pdf-key', 'failed.pdf')
                paper.pdf.name = pdf_key
                paper.save()

                def process(paper):
                    pdf_to_png_and_save(paper)
                    paper.text = get_text(paper)
                    try:
                        paper.save()
                    except DataError:
                        context = get_base_context(request)
                        context.update({
                            'message': {
                                'title': 'File Name Too Long',
                                'description': 'The file name of the PDF you just uploaded is too long. Please try to '
                                               'shorten it.'
                            }
                        })
                        return render(request, 'velarium/base.html', context)

                Thread(target=process, args=(paper,)).start()

            elif upload_option == UploadOption.LINK:
                link = request.POST.get('link', '')
                paper.link = link
                paper.save()
            else:
                raise NotImplementedError('Upload Option does not match any known type')
            update_tag(request, paper)
            return redirect('portal:index')
        else:
            context = get_base_context(request)
            return render(request, 'velarium/add-paper.html', context=context)
    else:
        raise Http404()

def install_keys(request):
    """
    This is a Django handler function for adding a paper into the database. This also handlers form submission through
    HTTP POST.
    :param request: The Django Request object
    :return: Depending on the request method, it either returns the upload UI, or a redirect to the index page
    """
    if get_user(request) and get_user(request).can_edit:
        if request.method == 'POST':

            paper = Paper(title=title, description=description)
            # Did not supply default value because it's better to crash and notify user and dev than silently fail.
            upload_option = UploadOption(int(request.POST['upload-option']))
            if upload_option == UploadOption.FILE:
                pdf_key = request.POST.get('pdf-key', 'failed.pdf')
                paper.pdf.name = pdf_key
                paper.save()

                def process(paper):
                    pdf_to_png_and_save(paper)
                    paper.text = get_text(paper)
                    try:
                        paper.save()
                    except DataError:
                        context = get_base_context(request)
                        context.update({
                            'message': {
                                'title': 'File Name Too Long',
                                'description': 'The file name of the PDF you just uploaded is too long. Please try to '
                                               'shorten it.'
                            }
                        })
                        return render(request, 'velarium/base.html', context)

                Thread(target=process, args=(paper,)).start()

            elif upload_option == UploadOption.LINK:
                link = request.POST.get('link', '')
                paper.link = link
                paper.save()
            else:
                raise NotImplementedError('Upload Option does not match any known type')
            update_tag(request, paper)
            return redirect('portal:index')
        else:
            context = get_base_context(request)
            return render(request, 'velarium/get-user.html', context=context)
    else:
        raise Http404()

def presign_s3(request):
    """
    The files stored in the AWS S3 bucket are not public and requires authentication for security reasons as the
    client might want to limit the access to only certain users. Only certain people should be able to edit the
    database. As the user might leak the credentials through negligence or incompetence, the presigned url is only
    limited to one file for a certain time frame. Function designed to be interacted programmatically.
    :param request: The Django Request object
    :return: A Json string of the credentials
    """
    if get_user(request).can_edit:
        file_name = request.GET['file_name']
        file_name = os.path.join(str(uuid.uuid4()), file_name)

        presigned_post = s3_client.generate_presigned_post(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Key=file_name,
            Fields={"Content-Type": 'application/pdf'},
            Conditions=[
                {"Content-Type": 'application/pdf'}
            ],
            ExpiresIn=600
        )
        return JsonResponse(presigned_post)
    else:
        raise Http404()


def edit_tags(request):
    """
    This is a Django handler function for editing the tag and tag class in the database
    :param request: The Django Request object
    :return: The edit tags page
    """
    if get_user(request) and get_user(request).can_edit:
        if request.method == 'POST':
            change_log = json.loads(request.POST['changeLog-json'])
            for new_tag_class in change_log['newTagClasses']:
                if new_tag_class['name']:
                    try:
                        TagClass.objects.get(name=new_tag_class['name'])
                    except TagClass.DoesNotExist:
                        TagClass(pk=uuid.UUID(new_tag_class['pk']), name=new_tag_class['name']).save()
            for new_tag in change_log['newTags']:
                if new_tag['name']:
                    tag_class = TagClass.objects.get(name=new_tag['tagClass'])
                    if not tag_class.tag_set.filter(name=new_tag['name']).exists():
                        Tag(pk=uuid.UUID(new_tag['pk']), name=new_tag['name'], tag_class=tag_class).save()
            for deleted_tag in change_log['deletedTags']:
                try:
                    Tag.objects.get(pk=deleted_tag).delete()
                except Tag.DoesNotExist:
                    logging.exception('Could not find tag in database')
            for deleted_tag_class in change_log['deletedTagClasses']:
                try:
                    TagClass.objects.get(pk=deleted_tag_class).delete()
                except TagClass.DoesNotExist:
                    logging.exception('Did not find tag class in database')

            return redirect('portal:edit-tags')
        else:
            context = get_base_context(request)
            return render(request, 'velarium/edit-tags.html', context=context)
    else:
        raise Http404()


def edit_paper(request, pk):
    """
    This is a Django handler function for editing the tags and names for existing papers.
    :param request: The Django Request object
    :param pk: The primary key of the paper
    :return: The edit paper page
    """
    if get_user(request) and get_user(request).can_edit:
        if request.method == 'POST':
            paper = Paper.objects.get(pk=pk)
            if request.POST.get('delete', 'off') == 'on':
                paper.delete()
                return redirect('portal:all-papers')
            else:
                paper.title = request.POST.get('title', '')
                paper.description = request.POST.get('description', '')
                paper.save()
                update_tag(request, paper)
                return redirect('portal:edit-paper', pk)
        else:
            context = get_base_context(request)
            context.update({
                'paper': Paper.objects.get(pk=pk),
            })
            return render(request, 'velarium/edit-paper.html', context=context)
    else:
        raise Http404()


def update_tag(request, paper):
    """
    This is a helper function that extract the tags in an HTTP POST form and update the tags for the paper object
    :param request: The Django Request object
    :param paper: the paper that needs to be updated
    :type paper: Paper
    :return: None
    """
    paper.tags.clear()
    for tag_class in TagClass.objects.all():
        tags = request.POST.getlist(str(tag_class.pk))
        for tag_pk in tags:
            tag = Tag.objects.get(pk=uuid.UUID(tag_pk))
            paper.tags.add(tag)
    paper.save()


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


def admin(request):
    """
    This is a Django handler function for the admin console
    :param request: The Django Request object
    :return: Rendered admin console page
    """
    if get_user(request) and get_user(request).is_admin:
        if request.method == 'POST':
            for user in User.objects.all():
                user.type = UserType[request.POST[user.pk].upper()]
                user.save()
            return redirect('portal:admin')
        else:
            context = get_base_context(request)
            context.update({
                'users': User.objects.all()
            })
            return render(request, 'velarium/admin.html', context=context)
    else:
        raise Http404()


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


def bookmark(request):
    """
    This is a Django handler function for bookmarking a paper. This can be accessed either programmatically or directly
    by the user
    :param request: The Django Request object
    :return: A redirection
    """
    user = get_user(request)
    if user:
        paper = Paper.objects.get(pk=request.GET['pk'])
        if user.bookmarks.filter(pk=paper.pk).exists():
            user.bookmarks.remove(paper)
        else:
            user.bookmarks.add(paper)
        return redirect('portal:index')
    else:
        raise Http404()


def bookmarked(request):
    """
    This is a Django handler for viewing all bookmarked papers
    :param request: The Django Request object
    :return: The results page
    """
    user = get_user(request)
    if user:
        context = get_base_context(request)
        context.update({
            'page_title': 'Bookmarked',
            'papers': user.bookmarks.all()
        })
        return render(request, 'velarium/results.html', context=context)
    else:
        raise Http404()
