from django.db import models


class Text(models.Model):
    text = models.TextField('Текст')

    def __str__(self):
        return self.text
