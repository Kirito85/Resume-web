from django.db import models

class Artiles(models.Model):

    title = models.CharField('Name' , max_length=50)
    anons = models.CharField('Anons', max_length=200)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Data')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "piece of news"
        verbose_name_plural = "news"