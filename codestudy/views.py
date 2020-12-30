from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
import logging
from .logins import get_user
from .models import TagClass, Tag, Paper, User
import os
from html import unescape
from .pdf_to_png import pdf_to_png
from threading import Thread
import json
import uuid
from django.conf import settings
from utils import s3_client
import google.oauth2.id_token
import google.auth.transport.requests
from django.core.exceptions import PermissionDenied


def get_base_context(request):
    return {
        'user': get_user(request),
        'tag_classes': TagClass.objects.all
    }


def index(request):
    if request.method == 'POST':
        return redirect('codestudy:index')
    else:
        context = get_base_context(request)
        return render(request, 'codestudy/index.html', context=context)


def results(request):
    context = get_base_context(request)
    context.update({
        'message': {
            'title': 'Search function is not implemented yet',
            'description': 'Try to use the tabs on top to navigate'
        }
    })
    return render(request, 'codestudy/results.html', context=context)


def browse(request, tag_class=None, tag=None):
    tag_class = unescape(tag_class)
    tag = unescape(tag)

    context = get_base_context(request)
    context.update({
        'papers': Tag.objects.get(name=tag, tag_class__name=tag_class).paper_set.all(),
    })
    return render(request, 'codestudy/results.html', context=context)


def all_papers(request):
    context = get_base_context(request)
    context.update({
        'papers': Paper.objects.all(),
        'all_papers': True
    })
    return render(request, 'codestudy/results.html', context=context)


def add_paper(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        paper = Paper(title=title, description=description)
        pdf_key = request.POST.get('pdf-key', 'failed.pdf')
        paper.pdf.name = pdf_key
        paper.save()
        update_tag(request, paper)
        Thread(target=pdf_to_png, args=(paper, paper.pdf)).run()
        return redirect('codestudy:index')
    else:
        context = get_base_context(request)
        return render(request, 'codestudy/add-paper.html', context=context)


def presign_s3(request):
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


def edit_tags(request):
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
                try:
                    Tag.objects.get(name=new_tag['name'])
                except Tag.DoesNotExist:
                    Tag(pk=uuid.UUID(new_tag['pk']), name=new_tag['name'],
                        tag_class=TagClass.objects.get(pk=new_tag['tagClass'])).save()
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

        return redirect('codestudy:edit-tags')
    else:
        context = get_base_context(request)
        return render(request, 'codestudy/edit-tags.html', context=context)


def edit_paper(request, pk):
    if request.method == 'POST':
        paper = Paper.objects.get(pk=pk)
        if request.POST.get('delete', 'off') == 'on':
            paper.delete()
            return redirect('codestudy:all-papers')
        else:
            paper.title = request.POST.get('title', '')
            paper.description = request.POST.get('description', '')
            paper.save()
            update_tag(request, paper)
            return redirect('codestudy:edit-paper', pk)
    else:
        context = get_base_context(request)
        context.update({
            'paper': Paper.objects.get(pk=pk),
        })
        return render(request, 'codestudy/edit-paper.html', context=context)


def update_tag(request, paper):
    paper.tags.clear()
    for tag_class in TagClass.objects.all():
        tags = request.POST.getlist(str(tag_class.pk))
        for tag_pk in tags:
            tag = Tag.objects.get(pk=uuid.UUID(tag_pk))
            paper.tags.add(tag)
    paper.save()


def login(request):
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
    context = get_base_context(request)
    return render(request, 'codestudy/admin.html', context=context)


def logout(request):
    try:
        del request.session['sub']
        success = True
    except KeyError:
        success = False
    return JsonResponse({'success': success})


def permission_denied(request):
    raise PermissionDenied


def handler404(request, exception):
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '404 Not Found',
            'description': 'This is no the web page you are looking for.',
        }
    })
    return render(request, 'codestudy/base.html', context=context)


def handler500(request):
    return render(request, 'codestudy/500.html')


def handler403(request, exception):
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '403 Permission Denied',
            'description': 'Looks like you don\'t have the permission to perform the action.'
        }
    })
    return render(request, 'codestudy/base.html', context=context)


def handler400(request, exception):
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '400 Bad Request',
            'description': 'Your client has issued a malformed or illegal request.'
        }
    })
    return render(request, 'codestudy/base.html', context=context)
