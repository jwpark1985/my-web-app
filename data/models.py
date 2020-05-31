from django.db import models
from django.conf import settings

# Create your models here.
class Source(models.Model):
    data_source = models.CharField(max_length=10)
    language = models.CharField(max_length=10)

    def __str__(self):
        return self.data_source

class Document(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sentence = models.TextField()
    label = models.CharField(max_length=10)
    data_source = models.ForeignKey(Source, on_delete=models.CASCADE)
    #created_date = models.DateTimeField(
    #        default=timezone.now)
    #published_date = models.DateTimeField(
    #        blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return '[%s] %s' % (self.label, self.sentence)


