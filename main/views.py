from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    """
    hello
    :return:
    """

    return HttpResponse('hello world')