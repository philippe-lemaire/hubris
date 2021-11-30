from django.db import models
from django.db.models.expressions import Case
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Territory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img_url = models.URLField(blank=True)
    description = MarkdownxField()

    def __str__(self):
        return self.name

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.description)


class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = MarkdownxField()
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.description)


class Rumor(models.Model):
    text = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
