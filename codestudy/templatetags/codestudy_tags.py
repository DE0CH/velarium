from django import template


register = template.Library()


@register.filter(name='is_bookmarked')
def is_bookmark(paper, user):
    return paper.is_bookmarked(user)
