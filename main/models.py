from django.db import models

class Note(models.Model):
    title = models.CharField()
    content = models.CharField()
    pub_date = models.DateTimeField("date published")
    

    def __str__(self) -> str:
        return self.title
    