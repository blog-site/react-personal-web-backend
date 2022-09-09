from django.db import models

class Archive(models.Model):
    class Meta:
        ordering = ["-date_published"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(primary_key=True, max_length=255, unique=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    # tags = models.ManyToManyField(Tag, blank=True)
