from django.db import models


class Thumbnails(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media', default='media/earth.png')
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
