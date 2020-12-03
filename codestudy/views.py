from django.shortcuts import render, redirect

from django.http import HttpResponse


def index(request):
    return render(request, 'codestudy/index.html')


def search_result(request):
    return render(request, 'codestudy/search-result.html', context={'search_terms': request.GET.get('search-terms', 'none')})