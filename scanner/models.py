from django.db import models

class Film(models.Model):
    title     = models.CharField(max_length = 1000)
    rating    = models.CharField(max_length = 3)
    director  = models.CharField(max_length = 2000)
    runtime   = models.CharField(max_length = 20)
    summary   = models.CharField(max_length = 10000)
    cast      = models.CharField(max_length = 10000)
    coverurl  = models.URLField()
    genre     = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.title
