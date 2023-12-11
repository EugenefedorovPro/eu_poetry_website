from django.db import models


class RawVerses(models.Model):
    id = models.AutoField(primary_key=True)
    html_name = models.CharField(max_length=50)
    date_of_writing = models.DateField(blank=True, null=True)
    title = models.TextField(null=True)
    verses = models.TextField(max_length=50000, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = "raw_verses"


class EuPro(models.Model):
    id = models.AutoField(primary_key=True)
    html_name = models.CharField(max_length=50, default="eupro")
    date_of_writing = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    fact = models.TextField(max_length=65535)

    def __str__(self):
        return str(self.id) + ". " + self.title

    class Meta:
        managed = True
        db_table = "eu_pro"
