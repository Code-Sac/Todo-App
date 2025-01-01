from django.db import models

# Create your models here.
class Todo(models.Model): #PascalCase models.Model is always needed(inheritate)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title