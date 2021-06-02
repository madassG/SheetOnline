from django.db import models


class Format(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название формата')
    code = models.CharField(max_length=100, verbose_name='Код формата')
    desc = models.CharField(max_length=1000, blank=True, verbose_name='Описание формата')

    def __str__(self):
        return self.name


class Sheet(models.Model):
    sheet_format = models.ForeignKey(Format, on_delete=models.SET_NULL, related_name='sheets', verbose_name='Формат ведомости', null=True)
    columns = models.CharField(max_length=30, verbose_name='Столбцы')
    file = models.FileField(upload_to='sheets', max_length=1000, verbose_name='Файл ведомости')
    response = models.TextField(max_length=5000, verbose_name='Вывод программы', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
