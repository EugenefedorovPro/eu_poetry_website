from django.test import TestCase
from django.urls import reverse
from .models import RawVerses, EuPro
from django.utils import timezone
import random


class EupoertyViewsTestCase(TestCase):
    databases = "__all__"

    def create_new_verse(self, html_name, title, date_of_writing, verses):
        return RawVerses.objects.create(
            html_name=html_name,
            title=title,
            date_of_writing=date_of_writing,
            verses=verses,
        )

    def create_new_eupro(self, title, fact):
        return EuPro.objects.create(
            title=title,
            fact=fact,
        )

    def test_html_name_rand_word(self):
        new_verse_1 = self.create_new_verse(
            html_name="html_name_verse_1",
            title="test_verse_1",
            date_of_writing=timezone.now(),
            verses="w1 w2 w3",
        )
        new_verse_2 = self.create_new_verse(
            html_name="html_name_verse_2",
            title="test_verse_2",
            date_of_writing=timezone.now(),
            verses="w4 w5 w6",
        )
        random.seed(6)
        response = self.client.get(reverse("content"))
        expected_output = [
            [new_verse_1.html_name, new_verse_1.verses.split()[2]],
            [new_verse_2.html_name, new_verse_2.verses.split()[0]],
        ]
        self.assertEqual(expected_output, response.context["html_name_rand_word"])

    def test_eupro(self):
        new_eupro_1 = self.create_new_eupro(
            title="title_of_new_eupro_1",
            fact="fact_of_new_eupro_1",
        )
        request = self.client.get(reverse("eupro"))
        request = self.client.get(reverse("eupro"))
        expected_output = new_eupro_1.fact
        self.assertEqual(expected_output, request.context["text"])
