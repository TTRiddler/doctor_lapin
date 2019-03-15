from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название документа')

    def get_document_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.name, ext)
        return 'documents/%s' % filename

    document = models.FileField(upload_to=get_document_url, max_length=100, verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Все документы'

    def __str__(self):
        return '%s' % self.name