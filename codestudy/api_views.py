from django.http import JsonResponse
from .models import Tag, TagClass


def index(request):
    return JsonResponse({})


def tags(request):
    tags = {}
    for tag_class in TagClass.objects.all():
        tag_group = []
        for tag in tag_class.tag_set.all():
            tag_group.append(tag.name)
        tags[tag_class.name] = tag_group
    return JsonResponse(tags)
