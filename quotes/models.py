from django.db import models

class Quotes(models.Model):
    said_by = models.CharField(max_length=200)
    quote = models.CharField(max_length=500)
    anime = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.said_by +' '+ self.quote +' '+self.anime
    
