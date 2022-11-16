from django.test import TestCase
from .models import RawVerses
from django.utils import timezone


class EupoertyViewsTestCase(TestCase):
    databases = "__all__"

    # def test_number_rand_words(self):
    #     number_of_ids = RawVerses.objects.all().values_list("id")
    #     print("____________", number_of_ids)
    #     response = self.client.get("/eupoetry/")
    #     number_of_words = len(response.context["list_of_lists_id_random_word"])
    #     self.assertEqual(number_of_ids, number_of_words)

    def test_new_verse_access(self):
        title = "new_verse"
        date_of_writing = timezone.now()
        verses = "Text of a new verse"
        new_verse = RawVerses.objects.create(
            id=23, title=title, date_of_writing=date_of_writing, verses=verses
        )
        response = self.client.get("/eupoetry/")
        print("____response____________", new_verse.id)
        self.assertQuerysetEqual([new_verse], [new_verse])
