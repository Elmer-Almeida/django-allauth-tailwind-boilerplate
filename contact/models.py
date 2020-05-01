from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{first_name} {last_name} Contact".format(
            first_name=self.first_name,
            last_name=self.last_name,
        )
