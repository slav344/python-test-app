from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата друку')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Надруковано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категорія')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новинa'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']
