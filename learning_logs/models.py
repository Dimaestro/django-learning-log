from django.db import models

# Create your models here.
class Topic(models.Model):
    ''' Тема которую изучает пользователь '''
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        ''' Возвращает строковое представление модели '''
        return self.text