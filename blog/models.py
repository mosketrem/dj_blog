from random import randint

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PostRecord(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    when_created = models.DateTimeField(auto_now_add=True)
    when_edited = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=203, db_index=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('view_blog_post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = "%s%s" % (slugify(self.title), randint(0,999))
        super().save(*args, **kwargs)
