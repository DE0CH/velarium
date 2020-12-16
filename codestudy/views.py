from django.shortcuts import render, redirect
from .logins import get_user
from .models import TagClass

from django.http import HttpResponse


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


def add_paper(request):
    if request.method == 'POST':
        # TODO: Implement ingest
        return redirect('codestudy:index')
    else:
        context = get_base_context(request)
        return render(request, 'codestudy/add-paper.html', context=context)
