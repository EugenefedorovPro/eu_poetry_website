# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RawVerses(models.Model):
    id = models.IntegerField(primary_key=True)
    date_of_writing = models.DateField(blank=True, null=True)
    title = models.TextField(null=True)
    verses = models.TextField(max_length=50000, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = "raw_verses"


class EuPro(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    fact = models.TextField(max_length=65535)

    def __str__(self):
        return str(self.id) + ". " + self.title

    class Meta:
        managed = True
        db_table = "eu_pro"
