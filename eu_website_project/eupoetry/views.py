from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .rand_words import get_random_words

# from models import RawVerses, IdWord, IdJsonWords

from .models import RawVerses, IdWord


# from pathlib import Path

# print("path cwd", Path.cwd())


def content(request):
    list_of_lists_id_random_word = get_random_words()
    template = loader.get_template("content.html")
    context = {"list_of_lists_id_random_word": list_of_lists_id_random_word}
    return HttpResponse(template.render(context, request))


def avva(request):
    template = loader.get_template("avva.html")
    return HttpResponse(template.render())


def bachinichego(request):
    template = loader.get_template("bachinichego.html")
    return HttpResponse(template.render())


def gdeyarostnej(request):
    template = loader.get_template("gdeyarostnej.html")
    return HttpResponse(template.render())
