from django.db import models


class FreeText(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Deneme(models.Model):
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.text


#deneme deneme