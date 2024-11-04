from django.db import models

# Create your models here.
class Lines(models.Model):
    name = models.CharField(max_length=128)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name