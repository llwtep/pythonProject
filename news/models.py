from django.db import models
from django.utils import timezone

# Create your models here.
class Articles(models.Model):
    title=models.CharField('Title of article', max_length=255)
    anons=models.CharField('Anons', max_length=255)
    full_text=models.TextField('The article')
    date = models.DateTimeField('Date', blank=True)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name='Article'
        verbose_name_plural='Articles'



