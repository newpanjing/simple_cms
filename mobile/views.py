# from django.shortcuts import render
from django import shortcuts


def render(request, template_name, context=None, content_type=None, status=None, using=None):
    return shortcuts.render(request, 'mobile/{}'.format(template_name), context, content_type, status, using)


def index(request):
    return render(request, 'base.html')
