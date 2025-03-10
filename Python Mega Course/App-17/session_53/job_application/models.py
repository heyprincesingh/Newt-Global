from django.db import models # type: ignore

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"