"""Module for views of the dnk app."""
from django.shortcuts import render


def index(request):
    return render(request, "index.html")
