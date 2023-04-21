from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'index.html')


def whoAmI(request):
    template = loader.get_template('aboutUs.html')
    return HttpResponse(template.render())
