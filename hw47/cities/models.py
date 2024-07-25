from django.db import models


class Cities(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='cities/images')

    def __str__(self):
        return self.title
