from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date_of_occurrence = models.DateTimeField()
    verdadeiro = models.BooleanField(default=False)
    age = models.IntegerField(default=0)

    def __str__(self):
        if len(self.text) > 20:
            return f'{self.author} - {self.text[:20]}...'
        return f'{self.author} - {self.text}'

class Teste(models.Model):
    nome = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.nome)