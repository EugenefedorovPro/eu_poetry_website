from django.db import models


class RawVerses(models.Model):
    id = models.AutoField(primary_key=True)
    html_name = models.CharField(max_length=50)
    title = models.TextField(null=True)
    text = models.TextField(max_length=50000, null=True)
    date_of_writing = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = "raw_verses"


class Hermeneutics(models.Model):
    id = models.AutoField(primary_key=True)
    raw_verses = models.ForeignKey(
        RawVerses,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    html_name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(max_length=65535)
    date_of_writing = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = "hermeneutics"


class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    raw_verses = models.ForeignKey(
        RawVerses,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    html_name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    audio = models.FileField(upload_to="audio/", null=True, blank=True)
    date_of_writing = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = "audio"

class EuPro(models.Model):
    id = models.AutoField(primary_key=True)
    html_name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(max_length=65535)
    date_of_writing = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ". " + self.title

    class Meta:
        managed = True
        db_table = "eu_pro"
