from django.db import models

# Create your models here.

class Searchs(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search

    # just rename this model
    class Meta:
        verbose_name_plural = 'Searches'