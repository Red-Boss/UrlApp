from django.db import models

class URLRecord(models.Model):
    url = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title