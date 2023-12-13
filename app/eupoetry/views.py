# import ipdb
from django.shortcuts import reverse, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import loader
from .rand_words import RandWord
from .models import RawVerses, EuPro, Hermeneutics, Audio
import random

def list_verses(request):
    verses = RawVerses.objects.all()
    context = {"verses": verses}
    return render(request, "list_verses.html", context)


def content(request):
    verse_html_name_rand_word = RandWord.get_verse_html_name_rand_word()
    fact_html_name_rand_word = RandWord.get_fact_html_name_rand_word()
    herm_html_name_rand_word = RandWord.get_herm_html_name_rand_word()
    context = {
        "verse_html_name_rand_word": verse_html_name_rand_word,
        "fact_html_name_rand_word": fact_html_name_rand_word,
        "herm_html_name_rand_word": herm_html_name_rand_word,
    }
    return render(request, "content.html", context)


def single_text(request, html_name):
    # selection between verse, herm, and eupro is based in type of url
    # herm = herm_<name>
    # possible issue, when they have the same url
    verse = RawVerses.objects.filter(html_name=html_name)

    if not verse:
        fact_obj = EuPro.objects.filter(html_name=html_name).first()

        if not fact_obj:
            fact_obj = Hermeneutics.objects.filter(html_name=html_name).first()
            verse = fact_obj.raw_verses

        context = {"fact_obj": fact_obj, "verse": verse}
        return render(request, "eupro.html", context)

    # get verse
    verse_obj = verse.first()

    # get interpretation to this verse if available
    verse_herm = verse_obj.hermeneutics_set.all().first()

    # get audio reading to this verse if available
    verse_audio = verse_obj.audio_set.all().first()

    context = {
        "verse": verse,
        "verse_herm": verse_herm,
        "verse_audio": verse_audio,
    }
    return render(request, "verse.html", context)


def eupro(request):
    all_ids = EuPro.objects.all().values_list("id")
    rand_id = random.choice(all_ids)[0]
    text = EuPro.objects.get(id=rand_id).text
    title = EuPro.objects.get(id=rand_id).title
    context = {"text": text, "title": title}
    return render(request, "eupro.html", context)


def back_to_content(request):
    url = reverse("content")
    return HttpResponseRedirect(url)
