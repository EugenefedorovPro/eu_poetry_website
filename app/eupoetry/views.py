# import ipdb
import random
import markdown2
from django.shortcuts import reverse, render
from django.http import HttpResponseRedirect
from .rand_words import RandWord
from .models import RawVerses, EuPro, Hermeneutics

def list_verses(request):
    tab = request.GET.get("tab")
    verses = RawVerses.objects.all().order_by("-date_of_writing")
    herms = Hermeneutics.objects.all().order_by("-date_of_writing")
    aesths = EuPro.objects.all().order_by("-date_of_writing")
    context = {"verses": verses, "herms": herms, "aesths": aesths, "tab": tab}
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
    # ipdb.set_trace()

    if not verse:
        fact_obj = EuPro.objects.filter(html_name=html_name).first()
        if fact_obj:
            fact_html = markdown2.markdown(fact_obj.text)

        elif not fact_obj:
            fact_obj = Hermeneutics.objects.filter(html_name=html_name).first()
            if fact_obj:
                fact_html = markdown2.markdown(fact_obj.text)
            try:
                verse = fact_obj.raw_verses
            except AttributeError:
                pass
        else:
            fact_html = "<span>что-то пошло не так<span>"

        context = {
            "fact_obj": fact_obj,
            "fact_html": fact_html,
            "verse": verse,
        }
        return render(request, "eupro.html", context)

    # get verse
    verse_obj = verse.first()
    verse_html = markdown2.markdown(verse_obj.text)

    # get interpretation to this verse if available
    verse_herm = verse_obj.hermeneutics_set.all().first()

    # get audio reading to this verse if available
    verse_audio = verse_obj.audio_set.all().first()

    context = {
        "verse_obj": verse_obj,
        "verse_html": verse_html,
        "verse_herm": verse_herm,
        "verse_audio": verse_audio,
    }
    return render(request, "verse.html", context)


def eupro(request):
    all_ids = EuPro.objects.all().values_list("id")
    rand_id = random.choice(all_ids)[0]
    fact_obj = EuPro.objects.get(id=rand_id)
    fact_html = markdown2.markdown(fact_obj.text)
    context = {"fact_obj": fact_obj, "fact_html": fact_html}
    return render(request, "eupro.html", context)


def back_to_content(request):
    url = reverse("content")
    return HttpResponseRedirect(url)
