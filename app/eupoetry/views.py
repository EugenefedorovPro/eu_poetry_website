# import ipdb
from django.shortcuts import reverse, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .rand_words import RandWord
from .models import RawVerses, EuPro, Hermeneutics
import random


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
    verse = RawVerses.objects.filter(html_name=html_name)
    # ipdb.set_trace()

    if not verse:
        fact_obj = EuPro.objects.filter(html_name=html_name).first()
        if not fact_obj:
            fact_obj = Hermeneutics.objects.filter(html_name=html_name).first()
        text = fact_obj.text
        title = fact_obj.title
        context = {"text": text, "title": title}
        return render(request, "eupro.html", context)


    context = {"verse": verse}
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
