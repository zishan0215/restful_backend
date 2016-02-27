from django.db import models

# Create your models here.

class Api(models.Model):
    connid = models.IntegerField()
    timeout = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.connid)
