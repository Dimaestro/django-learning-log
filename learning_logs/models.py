from django.db import models

# Create your models here.
class Topic(models.Model):
    ''' Тема которую изучает пользователь '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        ''' Возвращает строковое представление модели '''
        return self.text


class Entry(models.Model):
    ''' Информация изученная пользователем по теме '''
    topic = models.ForeignKey(Topic, on_delete=callable)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ''' Управление моделью '''
        # форма множественного числа при обращении более чем к одной записи Без этого Django будет использовать неправильную форму Entrys
        verbose_name_plural = 'entrise'

    
    def __str__(self):
        ''' Возвращает строковое представление модели '''
        return self.text[:50] + '...'
