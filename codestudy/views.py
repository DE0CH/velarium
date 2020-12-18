from django.shortcuts import render, redirect
import logging
from .logins import get_user
from .models import TagClass, Tag, Paper
from django.contrib.staticfiles.storage import staticfiles_storage
import os
from html import unescape
from .pdf_to_png import pdf_to_png
from threading import Thread
import json
import uuid


def get_base_context(request):
    return {
        'user': get_user(request),
        'tag_classes': TagClass.objects.all
    }


def index(request):
    if request.method == 'POST':
        print(request.POST.getlist('state', []))
        print(request.POST.getlist('checkbox', []))
        return redirect('codestudy:index')
    else:
        context = get_base_context(request)
        return render(request, 'codestudy/index.html', context=context)


def results(request):
    context = get_base_context(request)
    return render(request, 'codestudy/results.html', context=context)


def browse(request, tag_class=None, tag=None):
    tag_class = unescape(tag_class)
    tag = unescape(tag)

    context = get_base_context(request)
    context.update({
        'papers': Tag.objects.get(name=tag, tag_class__name=tag_class).paper_set.all(),
    })
    return render(request, 'codestudy/results.html', context=context)


def add_paper(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        paper = Paper(title=title, description=description)
        paper.save()
        for tag_class in TagClass.objects.all():
            tags = request.POST.getlist(tag_class.name, [])
            for tag_name in tags:
                tag = Tag.objects.get(name=tag_name, tag_class__name=tag_class.name)
                paper.tags.add(tag)
        pdf = request.FILES.get('pdf', open(staticfiles_storage.path('failed/failed.pdf')))
        paper.pdf.save(os.path.basename(pdf.name), pdf)
        Thread(target=pdf_to_png, args=(paper, paper.pdf)).run()
        return redirect('codestudy:index')
    else:
        context = get_base_context(request)
        return render(request, 'codestudy/add-paper.html', context=context)


def edit_tags(request):
    if request.method == 'POST':
        change_log = json.loads(request.POST['changeLog-json'])
        print(change_log)
        for new_tag_class in change_log['newTagClasses']:
            if new_tag_class['name']:
                try:
                    TagClass.objects.get(name=new_tag_class['name'])
                except TagClass.DoesNotExist:
                    TagClass(pk=uuid.UUID(new_tag_class['pk']), name=new_tag_class['name']).save()
        for new_tag in change_log['newTags']:
            print(new_tag)
            if new_tag['name']:
                try:
                    Tag.objects.get(name=new_tag['name'])
                except Tag.DoesNotExist:
                    Tag(pk=uuid.UUID(new_tag['pk']), name=new_tag['name'], tag_class=TagClass.objects.get(pk=new_tag['tagClass'])).save()
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
