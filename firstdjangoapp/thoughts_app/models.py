from django.db import models

# Create your models here.


class Thought(models.Model):
    mainText = models.CharField(max_length=100)
    # email = models.EmailField()
    # department = models.CharField(max_length=100)

    class Meta:
        app_label = 'thoughts_app'

    def __str__(self):
        return self.mainText
