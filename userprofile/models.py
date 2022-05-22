from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension

class Tracks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    track_name = models.CharField('Track name', max_length=50)
    source = models.FileField('Source', upload_to="sounds/", validators=[validate_file_extension], null=False)
    genre = models.CharField('Genre', max_length=50, default='None')
    auditions = models.IntegerField('Auditions', null=True, default=0)
    date = models.DateField('Release date', null=True)

    def __str__(self):
        return self.track_name

class Avatars(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.FileField('Image', upload_to="avatars/", null=False)
