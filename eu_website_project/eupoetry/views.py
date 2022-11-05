from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .rand_words import get_rand_word
from .models import RawVerses
from django.http import HttpResponseRedirect


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


def back_to_content(request, no_use):
    return HttpResponseRedirect("/eupoetry")
