from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .rand_words import get_rand_word
from .models import RawVerses, EuPro
from django.http import HttpResponseRedirect
import random


def content(request):
    rand_words = get_rand_word()
    list_of_lists_id_random_word = [
        [i_d + 1, word] for i_d, word in enumerate(rand_words)
    ]
    template = loader.get_template("content.html")
    context = {"list_of_lists_id_random_word": list_of_lists_id_random_word}
    return HttpResponse(template.render(context, request))


def verse(request, verse_id):
    verse = RawVerses.objects.filter(id=verse_id)
    template = loader.get_template("verse.html")
    context = {"verse": verse}
    return HttpResponse(template.render(context, request))


def eupro(request):
    total_number_ids = EuPro.objects.all().count()
    rand_id = random.randint(1, total_number_ids)
    text = EuPro.objects.get(id=rand_id).fact
    context = {"text": text}
    template = loader.get_template("eupro.html")
    return HttpResponse(template.render(context, request))


def back_to_content(request):
    return HttpResponseRedirect("/eupoetry")
