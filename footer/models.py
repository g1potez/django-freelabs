from django.db import models

class Support(models.Model):
    email = models.EmailField('Email', max_length=50)
    text = models.TextField('Text')

    def __str__(self):
        return self.email
