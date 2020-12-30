from django import template


register = template.Library()


@register.filter(name='is_bookmark')
def is_bookmark(paper, user):
    return paper.is_bookmark(user)
