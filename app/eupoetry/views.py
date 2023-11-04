from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .rand_words import RandWord
from .models import RawVerses, EuPro
import random


def content(request):
    html_name_rand_word = RandWord.make_list_html_name_rand_word()
    template = loader.get_template("content.html")
    context = {"html_name_rand_word": html_name_rand_word}
    return HttpResponse(template.render(context, request))


def verse(request, html_name):
    verse = RawVerses.objects.filter(html_name=html_name)
    template = loader.get_template("verse.html")
    context = {"verse": verse}
    return HttpResponse(template.render(context, request))


def eupro(request):
    all_ids = EuPro.objects.all().values_list("id")
    rand_id = random.choice(all_ids)[0]
    text = EuPro.objects.get(id=rand_id).fact
    context = {"text": text}
    template = loader.get_template("eupro.html")
    return HttpResponse(template.render(context, request))


def back_to_content(request):
    return HttpResponseRedirect("/eupoetry")
