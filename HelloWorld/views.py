from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>A HELLO FROM THE OTHER SIIIIIIIIIIDDDEEEEEEEEEE</h1>")