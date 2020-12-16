from django.shortcuts import render, redirect
from .logins import get_user
from .models import TagClass

from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        print(request.POST.getlist('state', []))
        print(request.POST.getlist('checkbox', []))
        return redirect('codestudy:index')
    else:
        context = {
            'user': get_user(request),
            'tag_classes': TagClass.objects.all
        }
        return render(request, 'codestudy/index.html', context=context)


def results(request):
    context = {
        'user': get_user(request)
    }
    return render(request, 'codestudy/results.html', context=context)


def add_paper(request):
    if request.method == 'POST':
        # TODO: Implement ingest
        return redirect('codestudy:index')
    else:
        context = {
            'user': get_user(request),
            'tags': map(''.join, Tag.objects.values_list('name')),
        }
        return render(request, 'codestudy/add-paper.html', context=context)